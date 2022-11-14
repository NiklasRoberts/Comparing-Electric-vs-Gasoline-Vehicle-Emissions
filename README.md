Electric Vehicles (EV) are often touted as an environmentally friendly alternative to traditional automobiles using an Internal Combustion Engine (ICE) which emit Carbon Dioxide (CO2) in the process of burning gasoline. Many Electric Vehicle manufacturers deceptively advertise their cars as "emission-free" because they emit no CO2 in the process of running. On the contrary, Electic Vehicles rely on local power generation to charge their batteries, so an EV emits as much CO2 as their local power grid. 

In this investigation I will use publicly available data to calculate and compare the amount of CO2 emitted from an ICE and the power grid which supplies an EV. I will investigate the US power grid averaged together, as well as each state's individual power supply.
Each state's power supply consists of some combination of Solar Thermal and Photovoltaic, Wind, Coal, Nuclear, Wood and Wood Derived Fuels and Other Biomass, Hydroelectric Conventional, Other Gases, Natural Gas, Petroleum, Geothermal, and Other.

According to the EIA, Solar, Wind, Nuclear, Biomass, Hydroelectric, and Geothermal energy sources all count as carbon neutral, meaning they emit no CO2 while producing energy.
Fossil Fuels (Coal, Other Gases, Natural Gas, Petroleum, and Other) all emit Carbon Dioxide in the process of generating power, just at different levels.
According to the EIA:
* Coal emits 2.230 lbs of CO2 while generating 1 kWh of energy
* Petroleum emits 2.195 lbs of CO2 while generating 1 kWh of energy
* Natural Gas emits 0.906 lbs of CO2 while generating 1 kWh of energy
* I assume that "Other Gases" emit the same amount of CO2 as Natural gas, so 0.906 lbs CO2/kWh
* I assume that "Other" sources emit the average of all fossil fuels, so 1.777 lbs CO2/kWh


To see the calculations for average CO2 emissions from an ICE, see CO2EmissionsFromICE.py
To see the calculations for average CO2 emissions from the United States power grid, see TotalCO2EmissionsFromEV.py
To see the calculations for average CO2 emissions from each state's power grid, see StateCO2EmissionsFromEV.py and StateResultsData/

Conclusions:
An Internal Combustion Engine burning traditional finished motor gasoline produces an average of 0.556 lbs of CO2 while generating 1 kWh of power.
The United States power grid as a whole produces an average of 0.853 lbs of CO2 while generating 1 kWh of power from various sources.




This investigation does not account for EV charged by personal solar panels, which would decrease CO2 emissions for a singular vehicle. 