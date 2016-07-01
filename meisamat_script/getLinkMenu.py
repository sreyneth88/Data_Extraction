import time
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
import traceback
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
#browser = webdriver.Firefox()
browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
def getLinkPro():
	url='http://meisamatr.com/'
	browser.get(url)
	
	try:
		linkpro=[]
		mainlink=browser.find_elements_by_css_selector("li:nth-child(2) > div > div > div > div.col-xs-12.col-sm-12.col-md-8.col-lg-8 > div > div > div div.content ul li a")
		print len(mainlink)
		for i in mainlink:
			getlink=i.get_attribute("href")
			print getlink
			link = io.open('linkmenu.csv', 'a', encoding='utf8')
			link.write(getlink+"\n")
	except NoSuchElementException:
		print "Not Found"
	try:
		otherlink=browser.find_elements_by_css_selector('li:nth-child(2) > div > div > div > div.col-xs-12.col-sm-12.col-md-4.col-lg-4 > div > ul > li > a')
		print len(otherlink)
		for i in otherlink:
			getlink=i.get_attribute("href")
			print getlink
			link = io.open('linkmenu.csv', 'a', encoding='utf8')
			link.write(getlink+"\n")
	except NoSuchElementException:
		print "Not Found"
	try:
		mainlink=browser.find_elements_by_css_selector("li:nth-child(3) > div > div > div > div.col-xs-12.col-sm-12.col-md-8.col-lg-8 > div > div > div div.content ul li a")
		print len(mainlink)
		for i in mainlink:
			getlink=i.get_attribute("href")
			print getlink
			link = io.open('linkmenu.csv', 'a', encoding='utf8')
			link.write(getlink+"\n")
	except NoSuchElementException:
		print "Not Found"
	try:
		otherlink=browser.find_elements_by_css_selector('li:nth-child(3) > div > div > div > div.col-xs-12.col-sm-12.col-md-4.col-lg-4 > div > ul > li > a')
		print len(otherlink)
		for i in otherlink:
			getlink=i.get_attribute("href")
			print getlink
			link = io.open('linkmenu.csv', 'a', encoding='utf8')
			link.write(getlink+"\n")
	except NoSuchElementException:
		print "Not Found"



try:
	getLinkPro()
	browser.quit()
except:
	print "Error script "
	traceback.print_exc()
	browser.quit()

	