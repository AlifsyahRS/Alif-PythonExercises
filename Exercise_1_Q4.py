#Part 2 Question 4
pi = 3.14 #Putting quotation marks will make 3.14 a string instead of a floating point value.
pie_diameter = 55.4 #a '.' cannot be used in a variable name. Use _ instead.
pie_radius = pie_diameter / 2 # // operator will always result into an integer, removing the possibility that the result could be a decimal number.
circumference = 2 * pi * pie_radius #Use only one '*' for multiplication as '**' will make the interpreter think that you want the exponent operator.
circumference_msg = "Jimmy's pie has a circumference: " # '-' cannot be used for naming variables. Also, using double quotation marks is a must if an apostrophe is present in the string.
print(circumference_msg, circumference)