# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:00:07 2019

@author: RUDRAJIT
"""
from selenium import webdriver

path=r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver"
browser=webdriver.Chrome(path)
link=r"https://www.seleniumhq.org"
#link=r"https://swayam.gov.in/nc_details/NPTEL"
browser.get(link)
#text="SIGN-IN / REGISTER"
#elem=browser.find_element_by_link_text(text)
#elem.click()
search=browser.find_element_by_id("q")
search.send_keys("Download")