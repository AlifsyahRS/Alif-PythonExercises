#Question 13 Answers
import string

user_input = input("Input a verb and this program will add an -ing prefix to it: ")
vowels = set('aeiou')
consonants = set(string.ascii_lowercase) - vowels

def makeForming(word):
    endwith_e = word.endswith('e')
    endwith_ie = word.endswith('ie')
    placeholder_list = []
    new_word = ''
    for char in word:
        placeholder_list.append(char)
    if endwith_ie == True:
        endwith_e = False
        del placeholder_list[-1:-3:-1]
        placeholder_list.append('ying')
    elif endwith_e == True:
        del placeholder_list[-1]
        placeholder_list.append('ing')
    elif placeholder_list[-1] and placeholder_list[-3] in consonants and placeholder_list[-2] in vowels:
        placeholder_list.append(placeholder_list[-1])
        placeholder_list.append('ing')
    else:
        placeholder_list.append('ing')
    for letter in placeholder_list:
        new_word += letter
    return new_word

print(makeForming(user_input))