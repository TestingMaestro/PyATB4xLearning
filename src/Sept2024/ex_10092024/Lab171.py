# using csv module to read csv file - comma separated
import csv
import pandas as pd
with open("TestData.csv", "r") as file:
    reader = csv.reader(file)
    for col in reader:
        print(col[0], col[1], sep="|")

# code can be reduced by using pandas library,
# pandas is a special library used to manipulate read csv data efficiently

read = pd.read_csv("TestData.csv")
print(read)
