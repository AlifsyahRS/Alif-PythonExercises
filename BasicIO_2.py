#Question 2
print("Given the force and mass, this program can determine an object's acceleration using Newton's 2nd Law of Motion.")

Force, Mass = input ("Please input the force (N) and mass (kg) of the object. Do it in this format (Force, mass): ").split(",")
Force = float(Force)
Mass = float(Mass)
Accel = Force / Mass

print ("The object is accelerating at a rate of", Accel, "ms^-2.")