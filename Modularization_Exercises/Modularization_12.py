#Question 12 Answers
user_input = input("Input a verb and this program will return the third person singular variant of said verb: ")
def make_suffix(word):
    Endwith_y = word.endswith('y')
    Endwith_o = word.endswith('o')
    Endwith_ch = word.endswith('ch')
    Endwith_s = word.endswith('s')
    Endwith_sh = word.endswith('sh')
    Endwith_x = word.endswith('x')
    Endwith_z = word.endswith('z')
    placeholder_list = []
    new_word = ''
    for char in word:
        placeholder_list.append(char)
    if Endwith_y == True:
        del placeholder_list[-1]
        placeholder_list.append('ies')
    elif Endwith_ch or Endwith_o or Endwith_s or Endwith_sh or Endwith_sh or Endwith_x or Endwith_z == True:
        placeholder_list.append('es')
    else:
        placeholder_list.append('s')
    for letter in placeholder_list:
        new_word += letter
    return new_word

print(make_suffix(user_input))