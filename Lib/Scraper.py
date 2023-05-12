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
        # desired_class_names = ['vmXl vmXl-mod-variant-large','c_cgF c_cgF-mod-variant-default','JWEO-stops-text','c_cgF c_cgF-mod-variant-default','vmXl vmXl-mod-variant-default','f8F1-price-text']

        driver = webdriver.Chrome()

        url="https://www.kayak.com/flights/JFK-ATH/2023-06-06?sort=bestflight_a"
        driver.get(url)
        sleep(10)

        # flights = driver.find_elements(By.CSS_SELECTOR, 'div.nrc6')
        # print(flights, len(flights))
        # for flight in flights:
        #     price = flight.find_element(By.CSS_SELECTOR, 'div.f8F1-price-text')
        #     print(price)
        wait = WebDriverWait(driver, 10)
        desired_class_names = ['vmXl vmXl-mod-variant-large','c_cgF c_cgF-mod-variant-default','JWEO-stops-text','c_cgF c_cgF-mod-variant-default','vmXl vmXl-mod-variant-default','f8F1-price-text']
        parent_elmnt_flights = driver.find_elements(By.XPATH, "//div[@class='nrc6']")
        for parent_elmnt_flight in parent_elmnt_flights:
            for class_name in desired_class_names:
                # desired_elmnts = parent_elmnt_flight.find_elements(By.XPATH, f".//*[contains(@class, '{class_name}')]")
                element = wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='nrc6']//*[contains(@class, '{class_name}')]")))

                for desired_elmnt in desired_elmnts:
                    flight_details = {
                        'Flight Time': desired_elmnt.text,
                        'Airline': desired_elmnt.text,
                        'Number of Stops': desired_elmnt.text,
                        'Layover Airport Code': desired_elmnt.text,
                        'Travel Duration': desired_elmnt.text,
                        'Price': desired_elmnt.text
                    }
                    
                    print(flight_details)
            



        


s=Scraper()

s.get_flights()

