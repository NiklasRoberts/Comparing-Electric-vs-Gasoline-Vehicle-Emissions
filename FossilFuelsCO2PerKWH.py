import pandas as pd

electricity_and_co2_by_source = pd.read_csv("Data/PowerAndCO2EmissionsBySource.csv")
lbs_per_kwh = {}


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

if __name__ == "__main__":
    print(lbs_per_kwh)