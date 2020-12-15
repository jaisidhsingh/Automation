from selenium import webdriver
import sys

class NBAcheck():
    def __init__(self):
        path = r"C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(path)

    def check_score(self):
        self.driver.get("https://www.nba.com/games")

    def watch_hits(self): 
        self.driver.get("https://www.youtube.com/channel/UCgDSF6FpenGam-wH747f1iw/videos")
    
    def team_hits(self):
        team = input("check team : ").lower()
        self.driver.get(f"https://www.youtube.com/results?search_query={team}+latest+match")
        
    def quit(self):
        self.driver.quit()

if sys.argv[1].lower() == "nba":
    while True:
        check = NBAcheck()
        check.check_score()
        inp = input("-> ").lower()
        if inp == "hits":
            check.watch_hits()
            done = input("done ? : ").lower()
            if done == "yes":
                break
            if done == "no":
                inp = input("-> ").lower()
        if inp == "team hits":
                check.team_hits()
                done = input("done ? : ").lower()
                if done == "yes":
                    break
                if done == "no":
                    inp = input("-> ").lower()
        if inp == "quit":
            check.quit()
            break


            
        





        



