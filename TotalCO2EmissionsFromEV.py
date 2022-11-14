# EIA considers electricity generation from biomass, hydro, solar, and wind to be carbon neutral.
# https://www.eia.gov/tools/faqs/faq.php?id=74&t=11

# Unlike fossil fuel-fired power plants, nuclear reactors do not produce air pollution or carbon dioxide while operating. However, the processes for mining and refining uranium ore and making reactor fuel all require large amounts of energy. Nuclear power plants also have large amounts of metal and concrete, which require large amounts of energy to manufacture. If fossil fuels are used for mining and refining uranium ore, or if fossil fuels are used when constructing the nuclear power plant, then the emissions from burning those fuels could be associated with the electricity that nuclear power plants generate.
# https://www.eia.gov/energyexplained/nuclear/nuclear-power-and-the-environment.php

# U.S. electric utility and independent power electricity generation and resulting CO2 emissions by fuel in 2020
# https://www.eia.gov/tools/faqs/faq.php?id=74&t=11

# Assumption: Electric Vehicles are charged using electricity generated from various power sources, so the CO2 emitted from electric vehicles is equivalent to the CO2 emitted from the average of all power sources used to generate the electricity
import pandas as pd

electricity_and_co2_by_source = pd.read_csv("Data/ElectrityAndCO2EmissionsBySource.csv")
# Renewable energy sources generate no CO2 emissions
# Assumption: Nuclear generates no CO2, ignoring possible emissions during supplies extraction for simplicity
# Assumption: The plants that are the source of biomass for energy capture almost the same amount of CO2 through photosynthesis while growing as is released when biomass is burned, which can make biomass a carbon-neutral energy source: https://www.eia.gov/energyexplained/biomass/biomass-and-the-environment.php
lbs_per_kwh = {renewable: 0 for renewable in ["Nuclear", "Wind", "Hydropower", "Solar", "Biomass", "Geothermal"]}


coal = electricity_and_co2_by_source.loc[electricity_and_co2_by_source["Sources"] == "Coal"]
# Unit: Million kWh
coal_electricity_generation = int(coal["Electricity Generation (million kWh)"])
# Unit: Million US tons
coal_CO2_produced = int(coal["CO2 Emissions (million US tons)"])
# Unit: lbs/kWh
lbs_per_kwh["Coal"] = round((coal_CO2_produced*2000)/coal_electricity_generation, 3)


nat_gas = electricity_and_co2_by_source.loc[electricity_and_co2_by_source["Sources"] == "Natural Gas"]
# Unit: Million kWh
nat_gas_electricity_generation = int(nat_gas["Electricity Generation (million kWh)"])
# Unit: Million US tons
nat_gas_CO2_produced = int(nat_gas["CO2 Emissions (million US tons)"])
# Unit: lbs/kWh
lbs_per_kwh["Natural Gas"] = round((nat_gas_CO2_produced*2000)/nat_gas_electricity_generation, 3)


petroleum = electricity_and_co2_by_source.loc[electricity_and_co2_by_source["Sources"] == "Petroleum"]
# Unit: Million kWh
petroleum_electricity_generation = int(petroleum["Electricity Generation (million kWh)"])
# Unit: Million US tons
petroleum_CO2_produced = int(petroleum["CO2 Emissions (million US tons)"])
# Unit: lbs/kWh
lbs_per_kwh["Petroleum"] = round((petroleum_CO2_produced*2000)/petroleum_electricity_generation, 3)


# Assumption: "Various gases" generate same emissions as natural gases
lbs_per_kwh["Other gases"] = lbs_per_kwh["Natural Gas"]
# Assumption: "Other sources" generates emissions equivalent to the average of all other fossil fuel sources
lbs_per_kwh["Other sources"] = sum([lbs_per_kwh[fossil_fuel] for fossil_fuel in ["Coal", "Natural Gas", "Petroleum"]])/3


electricity_generation_by_source = pd.read_csv("Data/ElectricityGenerationBySource.csv")
fuel_sources = ["Natural Gas", "Coal", "Petroleum", "Other gases", "Nuclear", "Wind", "Hydropower", "Solar", "Biomass", "Geothermal", "Other sources"]
percent_electricity_generation = {}
for fuel_source in fuel_sources:
    percent_electricity_generation[fuel_source] = float(electricity_generation_by_source.loc[electricity_generation_by_source["Fuel Sources"] == fuel_source]["Percent Electricity Generation"])


us_avg_lbs_per_kwh = 0
for fuel_source in fuel_sources:
    us_avg_lbs_per_kwh += lbs_per_kwh[fuel_source] * percent_electricity_generation[fuel_source]
us_avg_lbs_per_kwh = round(us_avg_lbs_per_kwh, 3)


if __name__ == "__main__":
    print("Fuel Source : Percent Total US Electricity Generation")
    for fuel_source, peg in percent_electricity_generation.items():
        print(f"{fuel_source} : {round(peg*100, 3)}%")
    print("\n")

    print("Fuel Source : CO2 (lbs) emitted in generating 1 kWh of electricity")
    for fuel_source, lbs_kwh in lbs_per_kwh.items():
        if lbs_kwh == 0:
            print(f"{fuel_source} : Carbon Neutral")
        else:
            print(f"{fuel_source} : {round(lbs_kwh, 3)} lbs CO2/kWh")
    print("\n")

    print(f"CO2 emissions in the US to generate 1 kWh of electricity: {us_avg_lbs_per_kwh} lbs, averaged among all energy production sources")