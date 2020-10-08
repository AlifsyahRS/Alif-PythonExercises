#Answer to Question 4

def calc_new_height():
    global curr_height, curr_width, des_width #Since variables weren't defined earlier, I used global to define them.
    curr_width = eval(input("Please enter the current width of the image: ")) #Line 5-7: User input
    curr_height = eval(input("Please enter the current height of the image: "))
    des_width = eval(input("Please enter the width you wish to use: "))
    new_height = curr_height*(des_width/curr_width) #Single slash division to make the result a float
    return new_height

print("The corresponding height to your width is:", calc_new_height())
