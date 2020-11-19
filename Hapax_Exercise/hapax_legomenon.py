from pathlib import Path
import string as st

list_punctuation = list(st.punctuation)
list_punctuation.remove("'")
list_digits = list(st.digits)


def hapax_legomenon(text):
    word_counter = {}
    hapax_counter = 0
    listofwords = text.lower().split()
    for word in listofwords:
        for char in word:
            if char in list_punctuation or char in list_digits:
                word = word.replace(char, '')
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1
    for i in word_counter:
        if word_counter[i] == 1:
            hapax_counter += 1
    return hapax_counter


def word_counter(sentence):
    word_count = 0
    for i in sentence.split(' '):
        word_count += 1
    return word_count


if __name__ == "__main__":
    # I managed to use pathlib to open the file without having to give the directory
    script_location = Path(__file__).absolute().parent
    file_location = script_location / 'formsofwater.txt'
    file = open(file_location, 'r', encoding='utf8')
    contents = file.read()
    ratio = hapax_legomenon(contents) / word_counter(contents) * 100
    print("\nNumber of Hapax Legomenon in the text: {} \nTotal number of words: {} \nRatio of Hapax Legomenon to total number of words: {}".format(
        hapax_legomenon(contents), word_counter(contents), ratio))
