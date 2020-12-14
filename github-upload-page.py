from selenium import webdriver
import time
import sys
import json

class GitUploadPage():
    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Program Files (x86)\chromedriver.exe")

    def login(self):
        with open("store.json") as f:
            data = json.load(f)
        username = data["username"]
        pw = data["password"]

        self.driver.get("https://github.com/")
        sign_in = self.driver.find_element_by_link_text("Sign in")
        sign_in.click()
        time.sleep(2)
        email_login = self.driver.find_element_by_id("login_field")
        email_login.send_keys(username)
        pw_login = self.driver.find_element_by_id("password")
        pw_login.send_keys(pw)
        pw_login.submit()
        time.sleep(3)
    
    def get_repo(self):
        automation_repo = self.driver.find_element_by_xpath('//*[@id="repos-container"]/ul/li[1]/div/a')
        automation_repo.click()
        time.sleep(3)

    def upload(self):
        self.driver.get(f"https://github.com/jaisidhsingh/{str(sys.argv[1])}/upload/main")
    def done(self):
        self.driver.quit()

        
test = GitUploadPage()
test.login()
test.get_repo()
test.upload()















