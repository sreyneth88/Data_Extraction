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
import csv
import traceback
from selenium.webdriver.support.ui import Select
import urllib
import json
import unicodedata
PYTHONIOENCODING='utf-8'

reload(sys)
sys.setdefaultencoding("UTF8")
browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

def getLinkMenu():
	browser.get("http://www.yslbeautyus.com/")
	browser.wait = WebDriverWait(browser, 40)
	time.sleep(2)
	try:
		linkMakeup=browser.find_elements_by_css_selector('li.cat_makeup > div > div > ul > li.level_2_list_item > ul > li.level_3_list_item > a')
		print len(linkMakeup)
		for i in linkMakeup:
			makeup=i.get_attribute("href")
			print makeup
			link = io.open('ysl_link_menu.csv', 'a', encoding='utf8')
			link.write(makeup+"\n")
	except NoSuchElementException:
		linkMakeup = ""
	try:
		linkFragrance=browser.find_elements_by_css_selector('li.cat_fragrance > div > div > ul > li > ul > div > li > a')
		print len(linkFragrance)
		for n in linkFragrance:
			fragrance=n.get_attribute("href")
			print fragrance
			link = io.open('ysl_link_menu.csv', 'a', encoding='utf8')
			link.write(fragrance+"\n")
	except NoSuchElementException:
		linkFragrance = ""
	try:
		morelinkfrag=browser.find_elements_by_css_selector('li.cat_fragrance > div > div > ul > li.level_2_list_item > ul > li > a')
		print len(morelinkfrag)
		for l in morelinkfrag:
			morelink=l.get_attribute("href")
			print morelink
			link = io.open('ysl_link_menu.csv', 'a', encoding='utf8')
			link.write(morelink+"\n")
	except NoSuchElementException:
		morelinkfrag =""
	try:
		linkSkin=browser.find_elements_by_css_selector('li.cat_skincare > div > div > ul > li.level_2_list_item > ul > li > a')
		print len(linkSkin)
		for p in linkSkin:
			skin=p.get_attribute("href")
			print skin
			link = io.open('ysl_link_menu.csv', 'a', encoding='utf8')
			link.write(skin+"\n")
	except NoSuchElementException:
		linkSkin = ""

try:
	#title=sys.argv[1]
	getLinkMenu()
	browser.close()
except:
	print "Error"
	traceback.print_exc()
	browser.close()
	