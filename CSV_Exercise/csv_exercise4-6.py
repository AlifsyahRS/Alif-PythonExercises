from pathlib import Path
import datetime
# This file contains the solution for numbers 4-6


script_location = Path(__file__).absolute().parent
file_location = script_location / 'steps.csv'
new_fileloc = script_location / 'stepsv2.csv'
file = open(file_location, 'r')
contents = file.read()
data = contents.split('\n')


date_dict = {}
for line in range(0, len(data)):
    if line >= 1:
        temp_list = data[line].split(",")
        """
        After seeing that the empty data spans up to the entire day, I decided to just set the empty data to 0 as there was
        no data in the first place and that won't affect the rest of the data
        """
        if temp_list[0].strip('"') == 'NA':
            if temp_list[1] not in date_dict:
                date_dict[temp_list[1]] = [
                    [0], [temp_list[2].rstrip('"')]]
            else:
                date_dict[temp_list[1]][0].append(0)
                date_dict[temp_list[1]][1].append(
                    temp_list[2].strip('\"'))
        elif temp_list[1] not in date_dict:
            date_dict[temp_list[1]] = [[temp_list[0].strip('\"')], [
                temp_list[2].strip('"')]]
        elif temp_list[1] in date_dict:
            date_dict[temp_list[1]][0].append(temp_list[0].strip('"'))
            date_dict[temp_list[1]][1].append(temp_list[2].strip('"'))

str_tofile = '"steps, ""date"", interval, weekday/end"\n'


# Creating a function to find if a certain day is a weekday or weekend.
def find_day(date_inp):
    date_data = date_inp.strip('"').split("-")
    year, month, day = eval(date_data[0]), eval(
        date_data[1].lstrip("0")), eval(date_data[2].lstrip("0"))
    date_datetime = datetime.date(year, month, day)
    day_inweek = date_datetime.weekday()
    if day_inweek <= 4:
        return "Weekday"
    elif day_inweek == 5 or day_inweek == 6:
        return "Weekend"


if __name__ == '__main__':
    # Putting everything into one string so that it will be easy to write to the CSV file.
    for i in date_dict:
        date_dict[i].append(find_day(i))
        for j in range(0, len(date_dict[i][0])):
            str_tofile += '"{},{},{},{}"\n'.format(
                date_dict[i][0][j], i, date_dict[i][1][j], date_dict[i][2])

    with open(new_fileloc, 'w') as d:
        d.write(str_tofile)
