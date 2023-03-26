from TotalCO2EmissionsFromEV import us_avg_lbs_per_miles
from CO2EmissionsFromICE import avg_lbs_CO2_per_mile

ICE_to_EV_emissions = round(avg_lbs_CO2_per_mile / us_avg_lbs_per_miles, 3)

if __name__ == "__main__":
    print(f"The average Internal Combustion Engine automobile in the US emits {avg_lbs_CO2_per_mile} lbs CO2/mile driven.")
    print(f"The average Electric Vehicle in the US emits {us_avg_lbs_per_miles} lbs CO2/mile driven.")
    print(f"The average Internal Combustion Engine automobile emits {ICE_to_EV_emissions} times more CO2 than the average Electric Vehicle")
