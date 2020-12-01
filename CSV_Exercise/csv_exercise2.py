from pathlib import Path
import statistics

# Solution to question2
script_location = Path(__file__).absolute().parent
file_location = script_location / 'steps.csv'
file = open(file_location, 'r')
contents = file.read()
data = contents.split('\n')


date_dict = {}
for line in range(1, len(data)):
    temp_list = data[line].split(",")
    if temp_list[0].strip('"') == 'NA':
        pass
    elif temp_list[1] not in date_dict:
        date_dict[temp_list[1]] = [eval(temp_list[0].strip('"'))]
    elif temp_list[1] in date_dict:
        date_dict[temp_list[1]].append(eval(temp_list[0].strip('"')))


if __name__ == '__main__':
    for i in date_dict:
        print("Average number of steps ran in {}: {}".format(
            i.strip('"'), statistics.mean(date_dict[i])))
        print("Median of steps ran in {}: {} \n".format(
            i.strip('"'), statistics.median_grouped(date_dict[i])))
