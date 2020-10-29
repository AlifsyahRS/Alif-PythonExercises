this_list = ['helo', 'henlo', 'helo', 'hi', 'hi', 'hi', 'bye']


def wordfrequencies(mylist):
    output_dict = {}
    for i in mylist:
        if i in output_dict:
            output_dict[i] += 1
        else:
            output_dict[i] = 1
    return output_dict


print(wordfrequencies(this_list))
