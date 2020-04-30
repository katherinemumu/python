'''
katherinemumu
Apr 29 2020
This program will create a csv file with the content from a website
'''

from bs4 import BeautifulSoup
import requests
import csv

csv_file = open("cms_scrape.csv", "w")
csv_writer = csv.writer(csv_file)

csv_writer.writerow(["header", "summary", "youtube"])

source = requests.get("http://coreyms.com").text

soup = BeautifulSoup(source, "lxml")

for article in soup.findAll("article"):
    header = article.h2.a.text

    summary = article.find("div", class_="entry-content").text

    try:
        vid_id = article.find("iframe", class_="youtube-player")["src"]
        vid_id = vid_id.split("/")[4]
        vid_id = vid_id.split("?")[0]
        yt_link = f"https://youtube.com/watch?v={vid_id}"
    except Exception as e:
        yt_link = None

    print(header)
    print(summary)
    print(yt_link)
    print()

    csv_writer.writerow([header, summary, yt_link])

csv_writer.close()

