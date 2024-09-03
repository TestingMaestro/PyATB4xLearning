# Leap year
year = int(input("Enter the year\n"))


def leap_year(my_year):
    if (my_year % 4 == 0 and my_year % 100 != 0) or my_year % 400 == 0:
        return "Leap Year"
    else:
        return "Not a Leap Year"


res = leap_year(year)
print(res)

