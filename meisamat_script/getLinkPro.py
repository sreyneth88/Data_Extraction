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
def getLinkProduct ():
	with open('linkmenu.csv', 'rb') as f:
		for row in f:
			print row
			browser.get(row)
			browser.wait = WebDriverWait(browser, 20)
			try:
				pag=browser.find_elements_by_css_selector('ul.pagination li')
				print len(pag)
				numPage=len(pag) -1
				if numPage < 1:
					try:
						getprolink = browser.find_elements_by_css_selector('#products > div > div figure > a')
						print len(getprolink)
						for i in getprolink:
							print getprolink
							prodetail=i.get_attribute("href")
							print prodetail
							link = io.open('linkprodetail.csv', 'a', encoding='utf8')
							link.write(prodetail+"\n")
					except NoSuchElementException:
						print "Cannot Click"
				else:
					print "More then one"
					try:
						lastpage=browser.find_element_by_css_selector("ul.pagination li:nth-child("+str(numPage)+") a").get_attribute("textContent")
						print lastpage
						for i in range(1,int(lastpage)):
							urlpro = browser.current_url
							pig = '#/pagesize-16/page-'+str(i)
							alllink = urlpro+pig
							print alllink
							try:
								getprolink = browser.find_elements_by_css_selector('#products > div > div figure > a')
								print len(getprolink)
								for i in getprolink:
									print getprolink
									prodetail=i.get_attribute("href")
									print prodetail
									link = io.open('linkprodetail.csv', 'a', encoding='utf8')
									link.write(prodetail+"\n")
							except NoSuchElementException:
								print "Cannot Click"
							time.sleep(10)
					except NoSuchElementException:
						print "no pag"
			except NoSuchElementException:
				print "Pagination not found"


try:
	#url=sys.argv[1]
	getLinkProduct()
	browser.quit()
except NoSuchElementException:
	print "Error script "
	browser.quit()