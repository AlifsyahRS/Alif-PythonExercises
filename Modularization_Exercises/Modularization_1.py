#Answer to Question 1
user_input = eval(input("Please input an array of numbers (seperated by a comma(,)): "))

def list_convert(lst):
    list_convert = list(lst)
    return list_convert

print(user_input)
print(list_convert(user_input))