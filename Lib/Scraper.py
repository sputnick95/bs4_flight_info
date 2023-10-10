from time import sleep

from seleniumbase import Driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import datetime
import csv
import requests
import os
import uuid
import time

class Scraper:

    def __init__(self, departure_loc, destination, year, month, day):
        self.year = year
        self.month = month
        self.day = day
        self.departure_loc = departure_loc
        self.destination = destination
        self.flights = []




    def get_flights(self):
        #In list below: Flight times, Airline, # of Stops, Layover Airport Code, Travel Duration, Price
        # desired_class_names = ['vmXl vmXl-mod-variant-large','c_cgF c_cgF-mod-variant-default','vmXl vmXl-mod-variant-default','c_cgF c_cgF-mod-variant-default','vmXl vmXl-mod-variant-default','f8F1-price-text']


        driver = Driver(uc=True)
        url=f'https://www.kayak.com/flights/{self.departure_loc}-{self.destination}/{self.year}-{self.month}-{self.day}?sort=bestflight_a'
        driver.get(url)
        sleep(5)
        button_element = driver.find_element(By.XPATH, "//div[@role='button' and @class='ULvh-button show-more-button']")
        button_element.click()
        sleep(2)

        desired_class_names = ['vmXl vmXl-mod-variant-large', 'X3K_-segments', 'c_cgF c_cgF-mod-variant-default','vmXl vmXl-mod-variant-default','f8F1-price-text']
        parent_elmnt_flights = driver.find_elements(By.XPATH, "//div[@class='nrc6']")

        twoD_content = []
        ff = []

        test = []
        for trip in parent_elmnt_flights:

            specific_element = trip.find_element(By.XPATH, ".//div[@class='nrc6-content-section' and @role='button']")

            specific_element.click()
            sleep(2)

            # TEST
            # flight_num_elements = driver.find_elements(By.XPATH, "//div[@class='X3K_-segments']")

            # for element in flight_num_elements:
            #     flight_number = element.find_elements(By.XPATH, ".//div[@class='nAz5-carrier-text']")
            #     for i in flight_number:   
            #         if i.text not in test:                     
            #             test.append(i.text)

        # print(test)
            # ____________________________________________________________________________________

            # UNCOMMENT
            all_element_contents = []

            for i in desired_class_names:
                child_components = trip.find_elements(By.XPATH, f".//*[contains(@class, '{i}')]")
                if i == 'X3K_-segments':
                    sleep(1.5)
                    for element in child_components:
                        flight_number = element.find_elements(By.XPATH, ".//div[@class='nAz5-carrier-text']")
                        concatted_number = ''
                        for j in flight_number:
                            if j ==flight_number[-1]:
                                concatted_number += j.text
                            else:
                                concatted_number += j.text + '\n'                        
                        all_element_contents.append(concatted_number)
                
                elif i == 'c_cgF c_cgF-mod-variant-default':
                    cgF = []
                    iata_code_concat = ''
                    for ii in child_components:
                        if ii == child_components[-1]:
                            iata_code_concat += ii.text
                        else:
                            iata_code_concat += ii.text + '\n'
                    cgF.append(iata_code_concat)
                    all_element_contents.append(cgF)

                elif child_components:
                    for cc in child_components:
                        all_element_contents.append(cc.text)

            
            # ------------------------------------------------------------------------------------------------------------------------------

            # UNCOMMENT SECTION
            twoD_content.append(all_element_contents)
            indices_of_interest = [0,1,2,3,4,5]
            final_content = [all_element_contents[i] for i in indices_of_interest]
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            final_content.append(formatted_time)
            ff.append(final_content)
        # --------------------------------------------------------------------------------
        # UNCOMMENT SECTION
        col_names = ['ID','Flight_Times', 'FLIGHT_NUMBER', 'Airline_Company_and_Layover_AIRprt','Number_of_stops','Flight_Duration','Price','Time_of_data_pull']

        custom_folder_path = "/Users/zoepetropoulou/Development/code/post_flatiron"

        current_id = 1
        for row in ff:
            row.insert(0, current_id)
            current_id += 1
        

        print(ff)
        # ------------------------------------------------------------------------------------------------
        
        # csv_file = pd.read_csv('/Users/zoepetropoulou/Development/code/post_flatiron/testflight2.csv')


        # UCOMMENT
        csv_file_path = os.path.join(custom_folder_path, "10102023_raw_test.csv")
        with open(csv_file_path, 'w') as f:
            writer = csv.writer(f)
            writer.writerow(col_names)
            writer.writerows(ff)
        

        



