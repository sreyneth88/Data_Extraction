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

def getLinkPro(url):
	browser.get(url)
	browser.wait = WebDriverWait(browser, 40)
	time.sleep(2)
	try:
		linkpro=browser.find_elements_by_css_selector('div.action_product_block > div.product_actions > a.button.learnmorebutton')
		print len(linkpro)
		for i in linkpro:
			getlink=i.get_attribute("href")
			print getlink
			link = io.open('ysl_link_product.csv', 'a', encoding='utf8')
			link.write(getlink+"\n")
	except NoSuchElementException:
		linkpro = ""

try:
	url=sys.argv[1]
	getLinkPro(url)
	browser.close()
except:
	print "Error"
	traceback.print_exc()
	browser.close()
	