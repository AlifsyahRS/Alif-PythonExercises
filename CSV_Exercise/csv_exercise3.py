from pathlib import Path

# Solution to question 3
script_location = Path(__file__).absolute().parent
file_location = script_location / 'steps.csv'
file = open(file_location, 'r')
contents = file.read()
data = contents.split('\n')
data_dict = {}

for line in range(0, len(data)):
    if line == 0:
        for header in data[line].split(","):
            data_dict[header.strip().split('"')[1]] = []
    elif line >= 1:
        temp_list = data[line].split(",")
        data_dict['steps'].append(temp_list[0].strip('"'))


def calculate_na():
    empty_counter = 0
    for i in data_dict['steps']:
        if i == 'NA':
            empty_counter += 1
    return empty_counter


print("Total number of empty data:", calculate_na())
