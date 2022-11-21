import pandas as pd
import FossilFuelsCO2PerKWH
from copy import deepcopy

### Prepare dictionary mapping power source: lbs CO2 emitted per kwh energy generated
EV_lbs_per_kwh = deepcopy(FossilFuelsCO2PerKWH.lbs_per_kwh)

# Renewable energy sources generate no CO2 emissions
# Assumption: Nuclear generates no CO2, ignoring possible emissions during supplies extraction for simplicity
# Assumption: The plants that are the source of biomass for energy capture almost the same amount of CO2 through photosynthesis while growing as is released when biomass is burned, which can make biomass a carbon-neutral energy source
for renewable in ["Nuclear", "Wind", "Hydropower", "Solar", "Biomass", ]:
    EV_lbs_per_kwh[renewable] = 0

# Assumption: "Other gases" generate same emissions as natural gases
EV_lbs_per_kwh["Other gases"] = EV_lbs_per_kwh["Natural Gas"]
# Assumption: "Other sources" generates emissions equivalent to the average of all other fossil fuel sources
EV_lbs_per_kwh["Other sources"] = sum([EV_lbs_per_kwh[fossil_fuel] for fossil_fuel in ["Coal", "Natural Gas", "Petroleum"]])/3
# Assumption: "Geothermal" generates approximately 1% of fossil fuel emissions
EV_lbs_per_kwh["Geothermal"] = EV_lbs_per_kwh["Other sources"]/100


### Compute average CO2 emitted per kWh among all power sources
electricity_generation_by_source = pd.read_csv("Data/PowerGenerationBySource.csv")
fuel_sources = ["Natural Gas", "Coal", "Petroleum", "Other gases", "Nuclear", "Wind", "Hydropower", "Solar", "Biomass", "Geothermal", "Other sources"]
percent_electricity_generation = {}
for fuel_source in fuel_sources:
    percent_electricity_generation[fuel_source] = float(electricity_generation_by_source.loc[electricity_generation_by_source["Fuel Sources"] == fuel_source]["Percent Electricity Generation"])


us_avg_lbs_per_kwh = 0
for fuel_source in fuel_sources:
    us_avg_lbs_per_kwh += EV_lbs_per_kwh[fuel_source] * percent_electricity_generation[fuel_source]
us_avg_lbs_per_kwh = round(us_avg_lbs_per_kwh, 3)


if __name__ == "__main__":
    print("Fuel Source : Percent Total US Power Generation")
    for fuel_source, peg in percent_electricity_generation.items():
        print(f"{fuel_source} : {round(peg*100, 3)}%")
    print("\n")

    print("Fuel Source : CO2 (lbs) emitted in generating 1 kWh of power")
    for fuel_source, lbs_kwh in EV_lbs_per_kwh.items():
        if lbs_kwh == 0:
            print(f"{fuel_source} : Carbon Neutral")
        else:
            print(f"{fuel_source} : {round(lbs_kwh, 3)} lbs CO2/kWh")
    print("\n")

    print(f"CO2 emissions in the US to generate 1 kWh of power: {us_avg_lbs_per_kwh} lbs, averaged among all energy production sources")