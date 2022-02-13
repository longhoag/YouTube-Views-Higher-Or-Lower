import csv

global data
filename = "views-title-source.csv"
data = []

with open(filename, newline='') as csvfile:
    data = list(csv.reader(csvfile))

for i in range(len(data)):
    print(data[i][2])