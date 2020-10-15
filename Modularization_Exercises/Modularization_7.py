#Question 7 Answers
list1 = ['Hello','hi', 'greetings','Wassup']

def make_length_list(lst):
    len_list = []
    for i in lst:
        len_list.append(len(i))
    return len_list

print(make_length_list(list1))
