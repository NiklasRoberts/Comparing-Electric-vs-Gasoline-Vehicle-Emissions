# A Comparison of the CO2 Emissions From Automobiles Powered by Gasoline vs Electricity

Electric Vehicles are often touted as an environmentally friendly alternative to traditional automobiles which emit Carbon Dioxide (CO2) in the process of burning gasoline. 
Many Electric Vehicle manufacturers deceptively advertise their cars as "emission-free" because they emit no CO2 in the process of running. 
However, Electic Vehicles rely on the local power grid to charge their batteries, so an EV emits as much CO2 as the local energy generation sources. 


In this investigation the emissions from a traditional automobile are compared with the emissions from the US power grid as a whole, as well as each individual state's power grid, revealing that despite popular rhetoric and belief **the average Electric Vehicle in the US emits xx% more Carbon Dioxide than a traditional automobile**. 

As well, **the average Electric Vehicle emits more Carbon Dioxide than the average traditional automobile in 39 states**.

% chloropleth map

# Methodology

In this investigation, publicly available data from the EIA is used to calculate and compare the amount of Carbon Dioxide (CO2) emitted from an Internal Combustion Engine (ICE) vs the power grid which supplies an Electric Vehicle (EV). 

Power sources will be compared using units of lbs CO2/kWh, measuring the mass of Carbon Dioxide emitted in the process of generating 1 kWh of energy.

This investigation does not account for EVs charged by personal solar panels, which would decrease CO2 emissions for a singular vehicle. 

Calculations for ICEs can vary based on a multitude of factors, including make, model, year, size, and type of vehicle. For the purpose of this investigation ICEs will be treated as a singular entity using averages, however if the data were to be gathered then further work could be done to separate the calculations into different vehicle classes.

# Internal Combustion Engine (ICE)

The average Carbon Dioxide emissions from an ICE per kWh energy produced can be calculated through a series of unit conversions. 

Starting with the two core pieces of input data, let
* Goal = ICE's CO2 emissions/kWh energy generated
* A = CO2 emissions (kg)/gallon gasoline
* B = Energy generation (btu)/gallon gasoline

and for unit conversions let
* x = lbs/kg
* y = btu/kWh

Such that

![](Data/ICEequation.png)

### Sources:

* [CO2 Emissions](https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle#:~:text=typical%20passenger%20vehicle%3F-,A%20typical%20passenger%20vehicle%20emits%20about%204.6%20metric%20tons%20of,8%2C887%20grams%20of%20CO2)
* [Energy Generation](https://www.eia.gov/energyexplained/units-and-calculators/)
* Conversions: [btu/kWh](https://www.eia.gov/energyexplained/units-and-calculators/energy-conversion-calculators.php) and [lbs/kg](https://www.rapidtables.com/convert/weight/kg-to-pound.html)

# Power Grid Supplying Electric Vehicles (EV)

Underlying this investigation is the assumption that Electric Vehicles are charged using electricity generated from the power grid, so the CO2 emitted from electric vehicles is equivalent to the average CO2 emitted from all power sources used to generate the electricity

The weighted average of CO2 emissions per kWh of energy generated is calculated from the product of each power source and the percent of total energy supplied.

Let 
* Goal = Power grid's CO2 emissions/kWh energy generated
* S = Energy Sources
* i = Each energy source
* C<sub>i</sub> = CO2 emissions (lbs/kWh) for energy source
* P<sub>i</sub> = Percent of total energy generated for energy source

Such that

![](Data/EVequation.png)


The weighted average of lbs CO2/kWh is calculated for the US as a whole, as well as each individual state.


## Emissions For Each Energy Source

The United States's power supply consists of some combination of Coal, Petroleum, Natural Gas, Other Gases, Other (various combustion based methods), Solar, Wind, Hydroelectric, Geothermal, and Biomass.

| Energy Source  | Emissions (lbs CO2/kWh) | Explanation                                                                                                                   |
|---------------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Coal          | 2.230                   | Fossil Fuel                                                                                                                   |
| Petroleum     | 2.195                   | Fossil Fuel                                                                                                                   |
| Natural Gas   | 0.906                   | Fossil Fuel                                                                                                                   |
| Other Gases   | 0.906                   | Assumption: Emissions are equivalent to Natural Gas                                                                           |
| Other         | 1.777                   | Assumption: Emissions are equivalent to the fossil fuel average                                                               |
| Solar         | 0                       | Carbon Neutral                                                                                                                     |
| Wind          | 0                       | Carbon Neutral                                                                                                                     |
| Hydroelectric | 0                       | Carbon Neutral                                                                                                                     |
| Geothermal    | .017                    | Assumption: Emissions are approximately 1% of the fossil fuel average                                                                                                        |
| Nuclear       | 0                       | Assumption: Disregard possible emissions required to acquire nuclear fuel                                                     |
| Biomass       | 0                       | Although burning biological fuel emits CO2, the EIA considers biomass to be carbon neutral because of the carbon absorption from biological organisms|


### Sources:

* [Fossil Fuels](https://www.eia.gov/tools/faqs/faq.php?id=74&t=11)
* [Renewable](https://www.eia.gov/tools/faqs/faq.php?id=74&t=11)
* [Geothermal](https://www.eia.gov/energyexplained/geothermal/geothermal-energy-and-the-environment.php)
* [Nuclear](https://www.eia.gov/energyexplained/nuclear/nuclear-power-and-the-environment.php)
* [Biomass](https://www.eia.gov/energyexplained/biomass/biomass-and-the-environment.php)

## Energy Generation Source Data

### United States Power Grid

Source: https://www.eia.gov/tools/faqs/faq.php?id=427&t=3 from 2021

### State Power Grid


# Analysis:
An Internal Combustion Engine burning traditional finished motor gasoline emits an average of **0.556 lbs CO2/kWh**

The United States power grid as a whole produces an average of **0.853 lbs CO2/kWh** from various power sources.

To see the calculations for average CO2 emissions from an ICE, see CO2EmissionsFromICE.py

To see the calculations for average CO2 emissions from the United States power grid, see TotalCO2EmissionsFromEV.py

To see the calculations for average CO2 emissions from each state's power grid, see StateCO2EmissionsFromEV.py and StateResultsData/