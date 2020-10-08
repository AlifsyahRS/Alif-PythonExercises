#Question 5 Answers

print("This program takes a temperature in Fahrenheit and converts it into its Celsius and Kelvin form.")
#Defining the functions for conversion
def convert_to_celsius(arg_fahrenheit): #arg_ used for arguments in functions
    temp_celcius = (5/9) * (arg_fahrenheit - 32)
    return temp_celcius #temp_ used for return values of functions
def convert_to_kelvin(arg_celcius): 
    temp_kelvin = arg_celcius + 273.15
    return temp_kelvin

def convert_temp():
    fahrenheit = eval(input("Enter a temperature in Fahrenheit: ")) #User input for fahrenheit
    celcius = convert_to_celsius(fahrenheit) #celcius and kelvin without any prefix will be used for print statement and celcius -> kelvin conversion
    kelvin = convert_to_kelvin(celcius) #convert_to_kelvin(convert_to_celsius(fahrenheit)) is also possible but I just made them variables for the sake of organization
    print("\nInputted temperature in Fahrenheit:", fahrenheit, "\nTemperature in Celcius:", celcius, "\nTemperature in Kelvin:", kelvin)

convert_temp()