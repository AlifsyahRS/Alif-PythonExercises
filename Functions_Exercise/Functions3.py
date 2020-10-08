#Answer to Question 3
avog_number = 6.022*(10**23) #Variable to represent Avogadro's number

def num_atoms(grams,atomic_weight=196.97): #Makes default atomic_weight 196.97 if not specified
    atoms = avog_number*grams/atomic_weight #Operation to find atoms
    return atoms

print(num_atoms(10))
print(num_atoms(10,12.001))
print(num_atoms(10,1.008))
