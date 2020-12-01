from pathlib import Path

# Solution to question 1
script_location = Path(__file__).absolute().parent
file_location = script_location / 'steps.csv'
file = open(file_location, 'r')
contents = file.read()
data = contents.split('\n')


date_dict = {}
for line in range(0, len(data)):
    if line >= 1:
        temp_list = data[line].split(",")
        if temp_list[0].strip('"') == 'NA':
            pass
        elif temp_list[1] not in date_dict:
            date_dict[temp_list[1]] = eval(temp_list[0].strip('"'))
        elif temp_list[1] in date_dict:
            date_dict[temp_list[1]] += eval(temp_list[0].strip('"'))


if __name__ == "__main__":
    for i in date_dict:
        print("Number of steps in {}: {}".format(i.strip('"'), date_dict[i]))
