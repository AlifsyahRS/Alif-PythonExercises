# Dictionary Exercises Question 1

input_dict = {'hello': 1, 'a': 2, 'world': 'lol'}


def removekeys(mydict, keylist):
    for keyword in keylist:
        del (mydict[keyword])
    return mydict


print(removekeys(input_dict, ['hello', 'a']))
