parameters = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm',
              'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}


def encode(string):
    new_string = ''
    for char in string:
        if char in parameters.keys():
            new_string += parameters[char]
        else:
            new_string += char
    return new_string


def decode(string):
    new_string = ''
    for char in string:
        if char in parameters.values():
            for key in parameters:
                if parameters[key] == char:
                    new_string += key
        else:
            new_string += char
    return new_string


if __name__ == '__main__':
    intro = print(
        "This program can encode or decode a string using Caesar cipher.")
    user_input = input("Enter the string here: ")
    user_choice = int(input("1) Encode the string. \n2) Decode the string.\n"))
    if user_choice == 1:
        print(encode(user_input))
    elif user_choice == 2:
        print(decode(user_input))
    else:
        print("Invalid input.")