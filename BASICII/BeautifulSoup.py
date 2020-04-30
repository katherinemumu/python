'''
katherinemumu
Apr 29 2020
BeautifulSoup stuff
'''

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.yourtango.com/2018314733/30-best-office-quotes-of-all-time-for-all-the-dunderheads-in-the-room').text

soup = BeautifulSoup(source, 'lxml')

# print(soup.prettify())

div = soup.find("div", class_="node-container")

# print(div.prettify())

lst = div.findAll("p")

for i in lst:
    print(i.text)