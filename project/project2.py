from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("F:/Nitish/coding/Python/PRO-C127 web_scraping/virtual/chromedriver.exe")

browser.get(START_URL)
time.sleep(10)

stars_data = []


def scrape():
    page = requests.get("https://en.wikipedia.org/wiki/List_of_brown_dwarfs")
    soup = BeautifulSoup(page.content , "html.parser")
#while True:
    yo = 0
    tables = soup.find_all("table" , attrs={"class":"wikitable"})
    for table in tables:
        yo += 1
        if yo == 3:
            #print(tables)
            body = table.find("tbody")
            tr = body.find_all("tr")
            for each_tr in tr:
                temp_list = []
                td = each_tr.find_all("td")
                for index , each_td in enumerate(td):
                    if index in range(0 , 3):
                        try:
                            temp_list.append(each_td.find_all("a")[0].contents[0])
                        except:
                            temp_list.append("")
                    else:
                        try:
                            temp_list.append(each_td.contents[0])
                        except:
                            temp_list.append("")
                stars_data.append(temp_list)

scrape()
print(stars_data)


yoyo = []

for i in range(1 , len(stars_data)):
    name = stars_data[i][0]
    distance = stars_data[i][5]
    mass = stars_data[i][7]
    radius = stars_data[i][8]


    yah = [name , distance , mass , radius ]
    yoyo.append(yah)


headers = ["star_name" , "distance" , "mass" , "radius" ]
star_df = pd.DataFrame(yoyo , columns=headers)
star_df.to_csv("starzz.csv" , index = True , index_label="id")