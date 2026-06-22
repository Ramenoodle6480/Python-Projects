#######################################################################
# Program Filename: WindPower
# Author: Roman Anderson
# Date: 4/20/2026
# Description: Calculator for the windpower of a turbine
# Input: wind speed, efficiency, and blade radius
# Output: windpower
#######################################################################

#######################################################################
# Function: gather variables
# Description: prompts the user to input the needed variables
# Parameters: wind speed, blade radius, and efficiency
# Return values: none
# Pre-Conditions: none
# Post-Conditions: variables are valid values
#######################################################################

# Sets error code for ease of printing later
error = "-------invalid input, must be a number greater than 0-------"

# Indicates start of inputs
print("-------Input Values-------")

# Requests wind speed input
while True:
    try:
        WindSpeed = float(input("Wind Speed (m/s): ").replace(",",""))
        if WindSpeed > 0:
            break
        else:
            print(error)
    except ValueError:
        print(error)

# Requests blade radius input
while True:
    try:
        BladeRadius = float(input("Blade Radius (m): ").replace(",",""))
        if BladeRadius > 0:
            break
        else:
            print(error)
    except ValueError:
        print(error)

# Requests efficiency input
while True:
    try:
        Efficiency = float(input("Efficiency (%): ").replace(",",""))
        if Efficiency > 0:
            break
        else:
            print(error)
    except ValueError:
        print(error)

# Breaks up inputs and outputs for ease of viewing
print("-------Calculating-------")

#######################################################################
# Function: calculate and output maximum and actual power
# Description: plugs inputs into formula and outputs the answers
# Parameters: wind speed, blade radius, and efficiency
# Return values: Maximum and actual power
# Pre-Conditions: inputs are valid
# Post-Conditions: none
#######################################################################

# Plugs in inputs to formulas
PowerMax = 0.5 * 1.2 * (3.14159 * BladeRadius ** 2) * WindSpeed ** 3 / 1000

# Adjusts max power for efficiency
PowerActual = PowerMax * Efficiency / 100

# Displays outputs
print("Maximum Power:", round(PowerMax,1), "kW")
print("Actual Power:", round(PowerActual,1), "kW")