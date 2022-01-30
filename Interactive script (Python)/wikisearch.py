from urllib.request import urlopen
import json
import os
from tqdm import tqdm
import time


def searchHere():
    
    searchQuery = input("Enter your search query: ")

    if searchQuery == "":
        print("No query entered!!!")
        exit()

    url = "https://en.wikipedia.org/w/api.php?action=opensearch&search="+searchQuery

    progressBar()

    response = urlopen(url)

    data_json = json.loads(response.read())
    writeFile(data_json[3][0], searchQuery)


def writeFile(data, searchQuery):
    
    with open('logs.txt', 'a') as fp:
        fp.write("\n"+searchQuery+"  "+data)
    showRes(data)


def progressBar():
    
    for i in tqdm (range (30), desc="Loading…", ascii=False, ncols=75):
        time.sleep(0.01)


def showRes(data):
    print("Below is your Search URL         All queries are logged into 'logs.txt'")
    print(data)


searchHere()
