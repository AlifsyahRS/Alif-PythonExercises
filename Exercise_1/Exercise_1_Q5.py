#Part 2 Question 5
print("This program will help in calculating the wavelength of a wave given its speed and frequency")
speed = float(input("Please put the value of the velocity of the wave (unit: m/s): "))
frequency =  float(input("Now put the value of the frequency of the wave (unit: Hz): "))
wavelength = speed/frequency
print("Velocity:", speed, "m/s")
print("Frequency:", frequency, "Hz")
print("Calculated Wavelength:", wavelength, "m")