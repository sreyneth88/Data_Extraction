import time
import datetime
import io
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium import selenium
import selenium 
import re
from selenium.webdriver.support.ui import Select
import urllib
import json
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
browser=webdriver.Firefox()
def getSearch(key):
	browser.get("http://www.fragrantica.com/")
	try:
		txtsearch=browser.find_element_by_css_selector("div#searchbox input#qajax")
		txtsearch.send_keys(key)
		btnSearch=browser.find_element_by_css_selector("div#searchbox input#searchbtn")
		btnSearch.click()
		time.sleep(5)
	except NoSuchElementException:
		print "Not found bar search "
	try:
		link=browser.find_element_by_css_selector("div.resultsajax p>a:first-child").get_attribute("href")
		print link
	except NoSuchElementException:
		print "not found"
	obj={
		"Product_name":key,
		"Link": link
	}		
	
	myStr=json.dumps(obj)
	fs = open("link.json", 'a')
	fs.write(myStr+', \n')

try:
	key=sys.argv[1]
	if key!='':
		getSearch(key)
		browser.quit()
	else:
		print "key is empty"
except:
	print "Error Script"
	browser.quit()