#Answer to Question 1
print("This program aims to convert a certain amount of time into days.")

def convert_to_days(): #Defining user input
    global hours, min, sec #has to be global since these values will be used outside of the function
    hours = int(input("Please enter a number of hours: "))
    min = int(input("Please enter a number of minutes: "))
    sec = int(input("Please enter a number of seconds: "))

convert_to_days()

def get_days(): #Converting the user input into days
    global days
    days = hours/24 + min/1440 + sec/86400
    return days


if min >= 60 or sec >= 60: #To make sure that user doesn't input 60 or more as minutes or seconds
    print("Invalid input. Please make sure the amount of minutes and seconds are less than 60.")
    convert_to_days() #Goes back to user input if the input is invalid
else:
    print(round(get_days(),4), "days") #Prints the result of conversion given that user input is valid
