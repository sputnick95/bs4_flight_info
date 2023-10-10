from seleniumbase import Driver
import time

driver = Driver(uc=True)
driver.get("https://nowsecure.nl/#relax")
time.sleep(6)
driver.quit()