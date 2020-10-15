#Question 9 Answers
list1 = ['Hello','hi', 'greetings','Wassup']

def filter_long_words(lwords,n=0): #I just set an optional parameter because why not.
    new_list = []
    for i in lwords:
        if len(i) > n:
            new_list.append(i)
    return new_list

print(filter_long_words(list1,4))

