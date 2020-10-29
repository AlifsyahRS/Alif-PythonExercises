user_dict = {'hello': 1, 'bean': 1, 'world': 2,
             'Not a Keyword': 21, 'zero': 1, 'one': 0}


def findvalue(mydict, val):
    output_list = []
    for key in mydict:
        if mydict[key] == val:
            output_list.append(key)
    return output_list


print(findvalue(user_dict, 1))
