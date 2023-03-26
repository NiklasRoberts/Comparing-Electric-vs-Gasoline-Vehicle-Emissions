import pandas as pd
import FossilFuelsCO2PerKWH
from copy import deepcopy
import plotly.express as px
from CO2EmissionsFromICE import avg_lbs_CO2_per_kwh as avg_ICE_CO2_per_kwh
from CO2EmissionsFromICE import avg_lbs_CO2_per_mile as avg_ICE_CO2_per_mile

state_EV_lbs_per_kwh = deepcopy(FossilFuelsCO2PerKWH.lbs_per_kwh)

# The average electric car kWh per 100 miles (kWh/100 mi) is 34.6.
# This is based on 231 electric cars, built between 2000 and 2022, and their kWh/100 mi as stated on fueleconomy.gov (the official US government source for fuel economy information).
# https://ecocostsavings.com/average-electric-car-kwh-per-mile/
avg_EV_miles_per_kwh = 1/.346

# Assumption: "Other gases" generate same emissions as natural gases
state_EV_lbs_per_kwh["Other Gases"] = state_EV_lbs_per_kwh["Natural Gas"]
# Assumption: "Other" generates emissions equivalent to the average of all other fossil fuel sources
state_EV_lbs_per_kwh["Other"] = sum([state_EV_lbs_per_kwh[fossil_fuel] for fossil_fuel in ["Coal", "Natural Gas", "Petroleum"]])/3
# Assumption: "Geothermal" generates approximately 1% of fossil fuel emissions
state_EV_lbs_per_kwh["Geothermal"] = state_EV_lbs_per_kwh["Other"]/100

# Assumption: "Other Biomass" and "Wood and Wood Derived Fuels" are both considered biomass, which is treated as Carbon Neutral by the EIA
# Renewable energy sources generate no CO2 emissions
# Assumption: Nuclear generates no CO2, ignoring possible emissions during supplies extraction for simplicity
for renewable in ["Hydroelectric Conventional", "Solar Thermal and Photovoltaic", "Other Biomass", "Wind", "Wood and Wood Derived Fuels", "Nuclear"]:
    state_EV_lbs_per_kwh[renewable] = 0


# Source: Net Generation by State by Type of Producer by Energy Source 
# https://www.eia.gov/electricity/data/state/
state_power = pd.read_csv("Data/AnnualStatePowerGeneration.csv")
state_power = state_power.dropna(axis=1, how="all")

state_total_power_in_2021 = state_power.loc[(state_power["YEAR"] == 2021) & (state_power["TYPE OF PRODUCER"] == "Total Electric Power Industry")]

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

energy_sources = ['Solar Thermal and Photovoltaic', 'Wind', 'Other Biomass', 'Coal', 'Nuclear', 'Wood and Wood Derived Fuels', 'Hydroelectric Conventional', 'Other Gases', 'Other', 'Natural Gas', 'Petroleum', 'Geothermal', 'Total']

cols = ["LBS_CO2_PER_KWH", "LBS_CO2_PER_MILE"]
cols.extend(energy_sources)
output_df = pd.DataFrame(columns = cols, index=states)

### Compute average CO2 emitted per kWh among all power sources per state
for state in states:
    # Calculate percent power generation for each power type
    state_df = total_power_generation = state_total_power_in_2021.loc[(state_total_power_in_2021["STATE"] == state)]

    total_power_generation = int(state_df.loc[state_df["ENERGY SOURCE"] == "Total"]["GENERATION (Megawatthours)"])

    row = {"LBS_CO2_PER_KWH": 0, "LBS_CO2_PER_MILE": 0}

    state_lbs_per_kwh = 0
    total = 0
    for source in energy_sources:
        # check if the source exist in the state
        if source not in state_df["ENERGY SOURCE"].tolist():
            row[source] = 0
            continue
        elif source == "Total":
            continue
        source_power_generation = int(state_df.loc[state_df["ENERGY SOURCE"] == source]["GENERATION (Megawatthours)"])
        source_percent_generation = round(source_power_generation/total_power_generation, 3)
        
        row[source] = source_percent_generation
        total += source_percent_generation

        state_lbs_per_kwh += source_percent_generation * state_EV_lbs_per_kwh[source]
    
    row["Total"] = total
    row["LBS_CO2_PER_KWH"] = round(state_lbs_per_kwh, 3)
    row["LBS_CO2_PER_MILE"] = round(state_lbs_per_kwh / avg_EV_miles_per_kwh, 3)
    output_df.loc[state] = pd.Series(row)


if __name__ == "__main__":
    output_df.to_csv("StateResultsData/AllStates.csv")

    sorted_df = output_df.sort_values("LBS_CO2_PER_KWH")
    sorted_df.to_csv("StateResultsData/OrderedByEmissions.csv")

    states_with_less_emissions_per_mile = sorted_df[sorted_df["LBS_CO2_PER_MILE"] < avg_ICE_CO2_per_mile]
    states_with_less_emissions_per_mile.to_csv("StateResultsData/StatesWithLessEmissionsPerMileThanICE.csv")

    states_with_more_emissions_per_mile = sorted_df[sorted_df["LBS_CO2_PER_MILE"] >= avg_ICE_CO2_per_mile]
    states_with_more_emissions_per_mile.to_csv("StateResultsData/StatesWithMoreEmissionsPerMileThanICE.csv")

    # Emissions per kwh
    normalized_state_emissions = output_df.copy()
    normalized_state_emissions["Normalized CO2 Emissions"] = normalized_state_emissions["LBS_CO2_PER_KWH"].apply(lambda x: x - avg_ICE_CO2_per_kwh)
    normalized_state_emissions["States"] = normalized_state_emissions.index


    fig = px.choropleth(normalized_state_emissions,
                    locations='States', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Normalized CO2 Emissions',
                    color_continuous_scale=px.colors.diverging.PRGn_r,
                    color_continuous_midpoint=0,
                    title="Normalized CO2 Emissions (lbs CO2/kWh): Electric Vehicle (EV) Emissions Per State - Average Gasoline Vehicle (ICE) Emissions",
                    width=1200,
                    height=800,
                    )

    fig.update_layout( 
        # customize legend orientation & position
        legend=dict(
            title='Normalized CO2 Emissions Per kWh', orientation = 'h', y=1, yanchor="bottom", x=0.5, xanchor="center"
        )
    )
    fig.add_annotation(text="Darker means higher CO2 Emissions", y=0, showarrow=False)
    
    fig.write_image("StateResultsData/NormalizedStateEmissionsPerKWH.png")

    # Emissions per mile
    normalized_state_emissions = output_df.copy()
    normalized_state_emissions["Normalized CO2 Emissions"] = normalized_state_emissions["LBS_CO2_PER_MILE"].apply(lambda x: x - avg_ICE_CO2_per_mile)
    normalized_state_emissions["States"] = normalized_state_emissions.index


    fig = px.choropleth(normalized_state_emissions,
                    locations='States', 
                    locationmode="USA-states", 
                    scope="usa",
                    color='Normalized CO2 Emissions',
                    color_continuous_scale=px.colors.sequential.Blues,
                    title="Normalized CO2 Emissions (lbs CO2/mile): Electric Vehicle (EV) Emissions Per State - Average Gasoline Vehicle (ICE) Emissions",
                    width=1200,
                    height=800,
                    )

    fig.update_layout( 
        # customize legend orientation & position
        legend=dict(
            title='Normalized CO2 Emissions Per Mile', orientation = 'h', y=1, yanchor="bottom", x=0.5, xanchor="center"
        )
    )
    fig.add_annotation(text="Darker means higher CO2 Emissions", y=0, showarrow=False)
    
    fig.write_image("StateResultsData/NormalizedStateEmissionsPerMile.png")





