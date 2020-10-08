#Answer to Question 2

def calc_weight_on_planet(mass, gravity=23.1): #gravtity=23.1 makes the value of gravity 23.1 if the gravity argument isn't specified
    weight = mass*gravity/9.81 #Operation to find weight in the planet
    print("Original weight on Earth:", mass, "N. Weight in gravity of", gravity, "m/s^2:", weight, "N.")

calc_weight_on_planet(120,9.81)
calc_weight_on_planet(120)
calc_weight_on_planet(120,23.1)
