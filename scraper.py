from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("chromedriver.exe")
browser.get(START_URL)
time.sleep(10)

headers=["Name","Distance","Mass","Radius"]
scraped_data=[]

def scrape():
    soup=BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table", attrs={"class", "wikitable"})
    table_body = bright_star_table.find('tbody')
    table_rows = table_body.find_all('tr')
    for row in table_rows:
            table_cols = row.find_all('td')
            temp_list = []
    for a_tag in soup.find_all("th",attrs={"class","headerSort"}):
        th_tags=a_tag.find_all("th_tags")
        for col_data in table_cols:
            data = col_data.text.strip()
            temp_list.append(data)
            scraped_data.append(temp_list)
    star_data=[]
    for i in range(0,len(scraped_data)):
        name = scraped_data[i][1]
        distance = scraped_data[i][3]
        mass = scraped_data[i][5]
        radius = scraped_data[i][6]

        required_data = [name, distance, mass, radius,]
        star_data.append(required_data)
    with open("scraper_2.csv","w")as f:
            csvwriter=csv.writer(f)
            csvwriter.writerow(headers)
            csvwriter.writerows(star_data)

scrape()

