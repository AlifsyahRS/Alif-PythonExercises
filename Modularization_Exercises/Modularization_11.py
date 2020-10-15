#Question 11 Answers
user_input = input("Input anything and this program will tell you how frequent each character is typed.")


def char_freq(sentence):
    output = {}
    for char in sentence:
        if char in output:
            output[char] += 1
        else:
            output[char] = 1
    return output

print(char_freq(user_input))
    

