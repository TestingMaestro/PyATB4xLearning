import csv
import pandas as pd


def read_csv_by_csvread():
    with open("DataTest.csv", "r") as file:
        reader = csv.reader(file)
        for col in reader:
            for row in reader:
                print(col[0], row[1], sep="|")
                break


def read_csv_using_pandas_library():
    with open("DataTest.csv", "r") as file1:
        df = pd.read_csv(file1)
        print(df)
