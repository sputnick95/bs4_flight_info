from Scraper import Scraper

def start_scraper():
    departure_loc = input("Please enter your departure location: ")
    destination = input("Please enter destination: ")
    year = input("Enter year: ")
    month = input("Enter month: ")
    day = input("Enter day: ")

    s=Scraper(departure_loc, destination, year, month, day)
    s.get_flights()

def default_input_automatic_scraper(departure_loc='JFK', destination='ATH', year='2023', month='08', day='16'):
    s=Scraper(departure_loc, destination, year, month, day)
    s.get_flights()

default_input_automatic_scraper()