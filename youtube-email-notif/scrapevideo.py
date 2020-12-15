import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import subprocess

path = "C:\Program Files (x86)\chromedriver.exe"
browser = webdriver.Chrome(path)

url = "https://www.youtube.com/c/<channel-name-without-spaces>/videos"
browser.get(url)
my_video = browser.find_element_by_xpath("enter xpath here")
video_title = str(my_video.text) 
print(video_title)
my_video.click()

video_url = str(browser.current_url)
id = video_url.split("=")[1]
thumbnail_url = f"https://img.youtube.com/vi/{id}/maxresdefault.jpg"

try:
    data = {}
    with open("user.json") as f:
        data = json.load(f)

    data["image_url"] = thumbnail_url
    data["videos_url"] = video_url
    data["title"] = video_title

    with open("user.json", "w") as f:
        json.dump(data, f)

    run_file = subprocess.run(["python", "test.py"], shell=True)
    print("returncode : ", run_file.returncode)
except:
    print("error")
finally:
    browser.close()