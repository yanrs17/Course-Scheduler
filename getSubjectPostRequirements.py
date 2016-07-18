import requests
from bs4 import BeautifulSoup
import sqlite3

url = 'http://www.artsci.utoronto.ca/current/program/enrolment-instructions/program-codes-contacts'
subject_posts = {}

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
		# subject_posts[program_code] = title
		tpl = (program_code, title)
		subject_posts[tpl] = []


# ------------------------------------------- #
# Here we have a dictionalry of subject_posts #
# where the key is the program_code, the      #
# value is the title of the program.          #
# dict name: subject_posts		      #
# ------------------------------------------- #


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Firefox()
driver.get("https://degreeexplorer.utoronto.ca/degreeExplorer/login.xhtml")
# ------------------------------------------- #
# Assume the user below has 0 subject post    #
# selected. 				      #
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
# post, and save them into a dictionary.      #
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

for key_code in subject_posts:
# for key_code in subject_posts:

	addProgramFieldElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(addProgramFieldID))
	addButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(addButtonXpath))



	addProgramFieldElement.send_keys(key_code[0])
	addButtonElement.click()

	# new subject post added
	time.sleep(20)

	# processing

	html_source = driver.page_source
	soup = BeautifulSoup(html_source, "html.parser")

	post_requirements = soup.find(id = "TimelineForm:registrationPosts-planner-timeline-0:0:detailAssessments")
	requirement_table = post_requirements.find_all("li")


	print(key_code[0])
	print(key_code[1])
	for requirement in requirement_table:
		line = requirement.find_all('td')
		course_needed = line[-1]
		txt = course_needed.get_text()
		end_index = txt.index("Courses still required")
		req_txt = txt[:end_index]
		subject_posts[key_code].append(req_txt)
		print(req_txt)


	# delete the subject post

	print("\n")
	removeButton = ".//*[@id='TimelineForm:registrationPosts-planner-timeline-0:0:j_id1112']"
	removeElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(removeButton))
	removeElement.click()
	time.sleep(10)
