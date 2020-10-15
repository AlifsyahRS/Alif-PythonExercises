#Question 3 Answers
import calendar

theyear = eval(input("Please specify the year: "))
themonth = eval(input("Please input the month (as number): "))

def main():
    month = calendar.month(theyear,themonth, w=0, l=0)
    return month

print(main())