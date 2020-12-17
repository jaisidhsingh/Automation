from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import sys

path = r"C:\Program Files (x86)\chromedriver.exe"


class CheckProFootball():

	def __init__(self):
		self.driver = webdriver.Chrome(path)

	def checktable(self, league):
		keys = league.split(sep=" ")
		self.driver.get(f"https://www.skysports.com/{keys[0]}-{keys[1]}-table")

	def checkteams(self, team):
		if " " in team:
			team = team.split(sep=" ")
			output = ""
			for n in range(len(team)):
				output += str(team[n]) + "-"
				output = output.replace(output[-1], "")
			self.driver.get(f"https://www.skysports.com/{output}")
		else:
			self.driver.get(f"https://www.skysports.com/{team}")


	def checkhits(self):
		self.driver.get(f"https://www.youtube.com/user/tuankendy01/videos")

	def exit(self):
		self.driver.quit()


check = CheckProFootball()

league = input("check league : ").lower()
if league:
	check.checktable(league)
team = input("check team : ").lower()

if team:
	check.checkteams(team)

hits = input("check hits : ")
if hits.lower() == "y":
	check.checkhits()

final = input("final check : ")
if final.lower() == "done":
	check.exit()

