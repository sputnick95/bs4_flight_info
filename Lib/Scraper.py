from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests

import os

class Scraper:

    def __init__(self):

        self.price = None
        self.flights = []

    def get_flights(self):
        #In list below: Flight times, Airline, # of Stops, Layover Airport Code, Travel Duration, Price
        # desired_class_names = ['vmXl vmXl-mod-variant-large','c_cgF c_cgF-mod-variant-default','vmXl vmXl-mod-variant-default','c_cgF c_cgF-mod-variant-default','vmXl vmXl-mod-variant-default','f8F1-price-text']

        driver = webdriver.Chrome()

        url="https://www.kayak.com/flights/JFK-ATH/2023-06-06?sort=bestflight_a"
        driver.get(url)
        sleep(7)

        desired_class_names = ['vmXl vmXl-mod-variant-large','c_cgF c_cgF-mod-variant-default','vmXl vmXl-mod-variant-default','f8F1-price-text']
        parent_elmnt_flights = driver.find_elements(By.XPATH, "//div[@class='nrc6']")


        for i in desired_class_names:
            child_components = parent_elmnt_flights[0].find_elements(By.XPATH, f".//*[contains(@class, '{i}')]")
            if child_components:
                for cc in child_components:
                    print(cc.text)
                print('----------')



                    
            



        


s=Scraper()

s.get_flights()

