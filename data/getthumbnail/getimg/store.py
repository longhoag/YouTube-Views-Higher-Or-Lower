import csv

global itemArray
filename = "Title-Thumb-Updated.csv"

itemArray = []

with open(filename, newline='') as csvfile:
    inputItem = list(csv.reader(csvfile))

for i in range(0,len(inputItem)):
    print(inputItem[i][1] + ',')