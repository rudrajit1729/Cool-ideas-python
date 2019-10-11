# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:28:16 2019

@author: RUDRAJIT
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
path=r"C:\Users\HP\Downloads\chromedriver_win32\chromedriver"
driver=webdriver.Chrome(path)
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver,600)
target='"Adrish"'#Enter friends name here
string='hi'#message that needs to be sent
#locating span tag elements
x_arg="//span[contains(@title,"+target+")]"
target=wait.until(EC.presence_of_element_located((By.XPATH,x_arg)))
target.click()

input_box=driver.find_element_by_class_name("_13mgZ")
for i in range(1):
    input_box.send_keys(string+Keys.ENTER)

    