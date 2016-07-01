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

def getDetail(url):
	browser.get(url)
	browser.wait = WebDriverWait(browser, 40)
	time.sleep(2)

	try:
		titles=browser.find_element_by_css_selector('div.pdp_top_content_wrapper > h1').get_attribute('textContent')
		print titles
	except NoSuchElementException:
		titles = ""
	try:
		price=browser.find_element_by_css_selector('fieldset > div.price.b-price > p').get_attribute('textContent')
		print price
	except NoSuchElementException:
		price = ""
	try:
		img=browser.find_element_by_css_selector('#wrap > a > img:nth-child(1)').get_attribute('src')
		print img
	except NoSuchElementException:
		img = ""
	try:
		clickrm=browser.find_element_by_css_selector('#tab_details > p > a').click()
	except NoSuchElementException:
		clickrm = ""
	try:
		des=browser.find_element_by_css_selector('body > div.productdetails_readmore_container > div.content > div > p').get_attribute('textContent')
		print des
	except NoSuchElementException:
		des = ""
	try:
		valuesize=[]
		size=browser.find_elements_by_css_selector('#va-sizeSelectBoxItOptions > li')
		print len(size)
		for l in size:
			getSize=l.get_attribute("textContent")
			print getSize
			valuesize.append(getSize)
	except NoSuchElementException:
		size = ""
	try:
		value=[]
		clickcolor=browser.find_elements_by_css_selector('#product_content > div.color_selectbox_wrapper > select > option')
		for n in clickcolor:
			if n == 1:
				print "Select Color"
			else:
				getcolor=n.get_attribute('value')
				print getcolor
				value.append(getcolor)
	except NoSuchElementException:
		clickcolor = ""

	obj = {
		"Title":titles,
		"Price":price,
		"Description":des,
		"ImageUrl": img,
		"Color":value,
		"Size":valuesize
	}

	myStr=json.dumps(obj)
	fs = open("ysl_product.json", 'a')
	fs.write(myStr+",\n")

try:
	url=sys.argv[1]
	getDetail(url)
	browser.close()
except:
	print "Error"
	traceback.print_exc()
	browser.close()
	