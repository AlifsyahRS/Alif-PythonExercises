#Question 8 Answers
list1 = ['Hello','hi', 'greetings','Wassup']

def longest_word(lwords):
    the_word = max(lwords, key=len)
    return the_word

print(longest_word(list1))


