import csv

global two_items
filename1 = "views-title.csv"
two_items = []

global one_item
filename2 = "imageSource-update.csv"
one_item = []

with open(filename1, newline='') as csvfile:
    two_items = list(csv.reader(csvfile))

with open(filename2, newline='') as csvfile:
    one_item = list(csv.reader(csvfile))

for i in range(len(two_items)):
    print(two_items[i][0] + ',' + two_items[i][1] + ',' + one_item[i][0] + ',')