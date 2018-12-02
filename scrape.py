########################
User: Stanley Nguyen
########################

import pandas as pd
from bs4 import BeautifulSoup
from splinter import Browser

def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)

def scrape ():
    
    browser = init_browser()
    mars_data = {}

    local_nasa_file = "News_Nasa_Mars_Exploration_Program.html"
    nasa_html = open(local_nasa_file, "r").read()
    news_soup = BeautifulSoup(nasa_html, "html.parser")
    news_soup

    news_list = news_soup.find('ul', class_='item_list')
    first_item = news_list.find('li', class_='slide')
    first_title = first_item.find('div', class_='content_title').text
    first_para = first_item.find('div', class_='rollover_description_inner').text
    mars_data['first_title']=first_title
    mars_data['first_para']=first_para

    browser.quit()

    return mars_data