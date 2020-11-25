from pathlib import Path
import random
import time


script_location = Path(__file__).absolute().parent
file_location = script_location / 'Pokemon.txt'
file = open(file_location, 'r')
content = file.read()
pokemon_list = content.split()


def game(mylist):
    sequence_list = []
    start_letter = random.choice(mylist)
    sequence_list.append(start_letter)
    output_string = ''
    for a in mylist:
        if a.startswith(start_letter[-1]) == True:
            sequence_list.append(a)
            break
    """
    Because of the timeout, it will take a while to execute the code but if I don't force a break, 
    the program would keep on going because there are some dead ends wherein there is no word that starts with the
    specific letter
    """
    timeout = time.time() + 2
    while len(mylist) > len(sequence_list):
        for a in mylist:
            random_select = random.choice(mylist)
            if random_select in sequence_list:
                pass
            elif random_select.startswith(sequence_list[-1][-1]) == True:
                sequence_list.append(random_select)
                break
        if time.time() > timeout:
            break
    for i in sequence_list:
        if i == sequence_list[-1]:
            output_string += i
        else:
            output_string += i + ', '
    return output_string


print(game(pokemon_list))
