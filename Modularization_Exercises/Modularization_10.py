#Question 10 Answers
import string

user_input = input("Input a sentence and this program will check if your sentence is a pangram or not.\n")

def check_pangram(sentence):
    char_list = set(sentence.lower())
    all_letters = set(string.ascii_lowercase)
    return bool(char_list >= all_letters)

if check_pangram(user_input) == True:
    print("This sentence is a pangram.")
else:
    print("This sentence is not a pangram.")
