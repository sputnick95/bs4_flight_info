from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

import os

class Scraper:

    def __init__(self, price):

        self.price = price
        self.flights = []

    def get_flights(self):

        departure_location='JFK'
        destination = 'ATH'
        url="https://www.kayak.com/flights/{departure_location}-{self.destination}/2023-06-06?sort=bestflight_a".format(departure_location=departure_location, destination=destination)
        doc = BeautifulSoup(requests.get(url).text,'html.parser')

        # for flight in doc.select('.nrc6'):
        for flight in range(0,6)
            price = flight.select('.f8F1-price-text').text if flight.select('.f8F1-price-text') else ''
            print(price)

