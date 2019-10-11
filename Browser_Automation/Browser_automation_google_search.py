# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 21:33:31 2019

@author: RUDRAJIT
"""

from selenium import webdriver
path=r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver"
text=input("Search Google:\n")
try:
    browser=webdriver.Chrome(path)
    link=r"https://www.google.com"
    browser.get(link)
    search=browser.find_element_by_name("q")
    search.send_keys(text+"\n")
except:
    print("Could not complete search..\nCheck your internet connection or try again later...")
    


