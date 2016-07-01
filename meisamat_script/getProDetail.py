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
import traceback
import json
import csv
reload(sys)
sys.setdefaultencoding("UTF8")
#browser = webdriver.Firefox()
browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')
def getProductDetail ():
	with open('linkprodetail.csv', 'rb') as f:
		for row in f:
			print row
			browser.get(row)
			browser.wait = WebDriverWait(browser, 20)
			try:
				title=browser.find_element_by_css_selector('#inner_product_details_left > div > header > h1').get_attribute('textContent')
				print title.encode('utf-8')
			except NoSuchElementException:
				title = ""
				print "Title not found"
			try:
				code=browser.find_element_by_css_selector('#inner_product_details_left > div > span.code.change-code').get_attribute('textContent')
				print code.encode('utf-8')
			except NoSuchElementException:
				code = ""
				print "Code not found"			
			try:
				price=browser.find_element_by_css_selector('#price > b').get_attribute("textContent")
				print price.encode('utf-8')
			except NoSuchElementException:
				price = ""
				print "Price not found"
			try:
				img=browser.find_element_by_css_selector('#magnifier-item-0').get_attribute("src")
				print img
			except NoSuchElementException:
				img = ""
				print "Img not found"
			try:
				urlpro = browser.current_url
				print urlpro
			except NoSuchElementException:
				urlpro = ""
				print "Url not found"
			try:
				size=browser.find_element_by_css_selector('#inner_product_details_left > div > div.inner_product_content_bottom > div.product_option_box.product_info_garanties > ul > li > label > span').get_attribute('textContent')
				print size
			except NoSuchElementException:
				size = ""
				print "Size not found"
			try:
				des=browser.find_element_by_css_selector('#inner_product_description > header').get_attribute("textContent")
				print des.encode('utf-8')
			except NoSuchElementException:
				des = ""
				print "Description not found"
			try:
				cat=browser.find_element_by_css_selector('#main > section > div > div > div > ul > li:nth-child(1)').get_attribute('textContent')
				print "Cat"+cat.encode('utf-8')
			except NoSuchElementException:
				cat = ""
				print "Category not found"
			try:
				subcat=browser.find_element_by_css_selector('#main > section > div > div > div > ul > li:not(:first-child)').get_attribute('textContent')
				print "Subcat"+subcat.encode('utf-8')
			except NoSuchElementException:
				subcat = ""
				print "Sub Category not found"

			obj = {
			"Url":urlpro,
			"Title":title,
			"Price":price,
			"Description":des,
			"Barcode":code,
			"Size":size,
			"ImageUrl": img,
			"Category":cat,
			"Sub Category":subcat
			}
			
			myStr=json.dumps(obj)
			fs = open("ProductDetail.json", 'a')
			fs.write(myStr+",\n")
				
try:
	#url=sys.argv[1]
	getProductDetail()
	browser.quit()
except NoSuchElementException:
	print "Error script "
	browser.quit()