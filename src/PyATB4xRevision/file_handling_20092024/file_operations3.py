# working with csv

import pandas as pd
import csv

if __name__ == "__main__":
    with open("Test.csv", "r") as csv_file1:
        reader = csv.reader(csv_file1)
        for col in reader:
            if col[0] == "City" and col[1] == "State":
                continue
            print(col[0], col[1], sep=": ", end="\n")

with open("Test.csv", "r") as csv_file:
    read = pd.read_csv(csv_file)
    print(read)
