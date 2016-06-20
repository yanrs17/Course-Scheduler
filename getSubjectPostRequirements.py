import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'http://www.artsci.utoronto.ca/current/program/enrolment-instructions/program-codes-contacts'
subject_posts = {}
sp = []

r = requests.post(url)
s = BeautifulSoup(r.text, 'html.parser')
program_codes= s.find(id = "parent-fieldname-text")

table = program_codes.find_all('tr')
rows = table[3:]

for row in rows:
	info = row.find_all('td')
	if (len(info) != 1):
		program_code = info[0].get_text()
		title = info[1].get_text()
		subject_posts[program_code] = title
		sp.append(program_code)


# ------------------------------------------- #
# Here we have a dictionalry of subject_posts #
# where the key is the program_code, the      #
# value is the title of the program.          #
# dict name: subject_posts					  #
# ------------------------------------------- #


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Chrome()
driver.get("https://degreeexplorer.utoronto.ca/degreeExplorer/login.xhtml")
# ------------------------------------------- #
# Assume the user below has 0 subject post    #
# selected. 								  #
# ------------------------------------------- #
ZYuser = ""
ZYpwd = ""

userFieldID = "loginForm:utorid"
passFieldID = "loginForm:password"
loginButtonXpath = ".//*[@id='loginForm:login']"

userFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(userFieldID))
passFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(passFieldID))
loginButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginButtonXpath))

userFieldElement.clear()
userFieldElement.send_keys(ZYuser)
passFieldElement.clear()
passFieldElement.send_keys(ZYpwd)
loginButtonElement.click()
time.sleep(10)

# ------------------------------------------- #
# Log into the Degree Explore, use Planner    #
# for checking requirements of each subject   #
# post, and save them into a dictionary.	  #
# ------------------------------------------- #

plannerButtonXpath = ".//*[@id='j_id91:plannerMenu']"
plannerButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(plannerButtonXpath))
plannerButtonElement.click()
time.sleep(10)

# ------------- Planner Page ---------------- #

addProgramFieldID = "TimelineForm:postCode-planner-timeline-0"
addProgramFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(addProgramFieldID))

addButtonXpath = ".//*[@id='TimelineForm:addProgram-planner-timeline-0']"
addButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(addButtonXpath))

# -------------- Add Button Setted ---------- #

for key_code in sp:
# for key_code in subject_posts:
	addProgramFieldElement.send_keys(key_code)
	addButtonElement.click()

	# new subject post added
	time.sleep(20)

	# processing



# requirementsTableXpath = ".//*[@id='TimelineForm:registrationPosts-planner-timeline-0:0:detailAssessments']"
# requirementsTableElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(requirementsTableXpath))

# html_source = driver.page_source






	# delete the subject post


	removeButton = ".//*[@id='TimelineForm:registrationPosts-planner-timeline-0:0:j_id1112']"
	removeElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(removeButton))
	removeElement.click()
	time.sleep(10)


