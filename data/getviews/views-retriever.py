from bs4 import BeautifulSoup
import requests
import csv

global itemArray
filename = "Title-Links-Updated.csv"

itemArray = []

with open(filename, newline='') as csvfile:
    inputItem = list(csv.reader(csvfile))


# def retriever(url):
#     r = requests.get(url)
#     s = BeautifulSoup(r.text, 'html.parser')
#     title = s.select_one('meta[itemprop="name"][content]')['content']
#     views = s.select_one('meta[itemprop="interationCount"][content]')['content']
#     data = {'title':title, 'views':views}
#     return data

# if __name__ == "__main__":
#     url ="https://www.youtube.com/watch?v=Vdm6i1m4tDE"
#     data = retriever(url)
#     print(data)

for i in range(len(inputItem)):   
    # url ='https://www.youtube.com/watch?v=Vdm6i1m4tDE'
    url = inputItem[i][1]
    soup = BeautifulSoup(requests.get(url).text, 'lxml')
    pr = soup.select_one('meta[itemprop="interactionCount"][content]')['content']
    print(pr + ',' + inputItem[i][0] + ',')
