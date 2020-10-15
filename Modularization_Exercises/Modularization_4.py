#Question 4 Answers
a = [2,3,5,7,11,69,420,'Hello','Goodbye','o_o']
user_input = eval(input("Just input anything: "))

def is_member(val,lst):
    index = 0
    boolean = False
    while len(lst) > index:
        if val == lst[index]:
            boolean = True
            break
        else:
            index += 1
    return boolean

print(is_member(user_input,a))
