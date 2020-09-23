#Question 1
print ("Please enter your height (in feet) and we'll find the right length for your snowboard")
Height_Ft = int(input("Feet (ft): "))
Height_In = int(input("Inches (in): "))
Convert_Ft = Height_Ft * 30.48
Convert_In = Height_In * 2.54
Snowboard = (Convert_Ft + Convert_In) * 0.88
print("Your are", Height_Ft, "feet and", Height_In, "inches tall.", "\nThe suggested length for your snowboard is", Snowboard, "centimeters.")