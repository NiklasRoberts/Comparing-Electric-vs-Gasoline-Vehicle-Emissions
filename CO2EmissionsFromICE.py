# CO2 Emissions from 1 gallon of gasoline can vary depending on the fuel efficiency and car model
# Assumption: We are comparing EV to traditional ICE using gasoline fuel
# Average kg CO2 emitted from burning one gallon of gasoline
avg_kg_CO2_per_gallon_gas = 8.887

lbs_per_kg = 2.205

avg_lbs_CO2_per_gallon_gas = round(avg_kg_CO2_per_gallon_gas * lbs_per_kg , 3)

# Energy produced from 1 gallon of finished motor gasoline (containing about 10% fuel ethanol by volume), measured in Btu (British Thermal Units)
avg_btu_per_gallon_gas = 120238

btu_per_kwh = 3412

avg_kwh_per_gallon_gas = round(avg_btu_per_gallon_gas / btu_per_kwh, 3)

# CO2/kWh = C02/gallon gas * gallon gas/kWh
avg_lbs_CO2_per_kwh = round(avg_lbs_CO2_per_gallon_gas / avg_kwh_per_gallon_gas, 3)

if __name__ == "__main__":
    print(f"Average CO2 emitted from an ICE burning 1 gallon of gasoline: {avg_lbs_CO2_per_gallon_gas} lbs")
    print(f"Average amount of energy generated from 1 gallon of gasoline: {avg_kwh_per_gallon_gas} kWh")
    print(f"Average CO2 emitted per kWh generated from an ICE burning gasoline: {avg_lbs_CO2_per_kwh} lbs")