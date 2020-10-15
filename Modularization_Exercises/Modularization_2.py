#Answer to Question 2


user_input = input("Type down a line of text and all consonants will be doubled with an o seperating them: ")
    
def translate(text):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    placeholder_list = []
    new_string = ''
    for char in text:
        placeholder_list.append(char)
    for i in placeholder_list:
        if i in vowels:
            new_string += i
        elif i == ' ':
            new_string += i
        else:
            i += 'o' + i
            new_string += i
    return new_string

print(translate(user_input))