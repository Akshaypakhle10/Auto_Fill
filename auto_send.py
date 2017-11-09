import csv
import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui

def send_certi(name1,event1,email1):
	browser = webdriver.Chrome()
	browser.get('http://localhost/digitalcerti/')
	wait = ui.WebDriverWait(browser,1)
	
	try:

		name = browser.find_element_by_css_selector('#name').send_keys(name1)
		event = browser.find_element_by_css_selector('#eventname').send_keys(event1)
		email = browser.find_element_by_css_selector('#email').send_keys(email1)
		issue = browser.find_element_by_css_selector('body > div > form > div:nth-child(4) > div > button').click()
		wait.until(lambda driver: driver.title.lower().startswith('Successfully Sent'))
	except TimeoutException:
		print("Done :", name1,",",event1,",",email1 )
	browser.close()

with open('test.csv','r') as f:
	r = csv.reader(f, delimiter=',')
	for row in r:
		if len(row)==3:
			send_certi(row[0],row[1],row[2])
		






