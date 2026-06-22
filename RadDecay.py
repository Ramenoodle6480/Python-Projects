#######################################################################
# Program Filename: RadDecay
# Author: Roman Anderson
# Date: 5/13/26
# Description: Calculates the activation and decay activity of aluminum
# Input: activation time and mass of aluminum
# Output: activation and decay activity
#######################################################################

#set error codes
error1 = "Invalid input, must be a number greater than 0"

#start inputs
print("Input Values")

#input 1
while True:
    try:
        mass = float(input("Mass of aluminum (g): ").replace(",",""))
        if mass > 0:
            break
        else:
            print(error1)
    except ValueError:
        print(error1)

#input 2
while True:
    try:
        time = float(input("Time to activate (s): ").replace(",",""))
        if time > 0:
            break
        else:
            print(error1)
    except ValueError:
        print(error1)

#calculate number of atoms
atoms = (mass * (6.022*10**23)) / 26.98

#start activation section
print("Activation")

#activation loop
timestep_a = 0
loopcount_a = int(time / 30)
while True:
    if timestep_a < loopcount_a:
        energy_a = ((10**8) * atoms * (231*(10**-24))) * (1 - (2.71828**(-0.005145 * (timestep_a + 1) * 30)))
        print("At time step",(timestep_a + 1) * 30, "seconds the activity is", round(energy_a, 2), "dps")
        timestep_a = timestep_a + 1
    else:
        energy_af = ((10**8) * atoms * (231*(10**-24))) * (1 - (2.71828**(-0.005145 * time)))
        print("The final activity from activation is", round(energy_af, 2), "dps")
        break

#start decay section
print("Decay")

#decay loop
timestep_d = 0
while True:
    energy_d = energy_af * (2.71828**(-0.005145 * (timestep_d + 1) * 30))
    if energy_d < (energy_af * 0.25):
        print("The final activity from decay is", round(energy_af * 0.25, 2), "dps")
        break
    else:
        print("At time step",(timestep_d + 1) * 30, "seconds the activity is", round(energy_d, 2), "dps")
        timestep_d = timestep_d + 1
