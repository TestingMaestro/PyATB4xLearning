# Leap year check

year = input("Enter the year\n")
year = int(year)

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")

#Logic 2
if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
