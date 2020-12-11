import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image

path = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)

if len(sys.argv) > 1:
    address = " ".join(sys.argv[1:])

driver.get('https://www.google.com/maps/place/' + address)
try:
    search = driver.find_element_by_xpath('''//*[@id="searchboxinput"]''')
    search.click()
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    directions = driver.find_element_by_xpath('''//*[@id="pane"]/div/div[1]/div/div/div[5]/div[1]/div/button/img''')
    directions.click()
    print("done")
except:
    print("error")
driver.save_screenshot("ss.png")
time.sleep(3)
image = Image.open("ss.png")
image.show()

