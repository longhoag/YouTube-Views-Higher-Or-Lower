import csv
import urllib.request

global itemArray 
filename = 'imageSource-update.csv'

itemArray = []

with open(filename) as csvfile:
    inputItem = list(csv.reader(csvfile))

def download_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

num = 0

for i in range(0, len(inputItem)):
    try:
        download_jpg(inputItem[i][0], '/Volumes/Ryan/Project/thumbnail', str(i))
    except:
        print(str(i+1))
        num = num + 1
        pass

print('total defects: ' + str(num))