#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import numpy as np


# In[2]:


options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'


# In[3]:


def website():
    driver.get('http://localhost:3000')
    time.sleep(2)
    driver.get('http://localhost:3000/createuser')

def login(user_id,passwrd):
    ksi = driver.find_element_by_class_name('input100')
    ksi.send_keys(user_id)
    time.sleep(2)
    ksi_pass = driver.find_element_by_name("password")
    ksi_pass.send_keys(passwrd)
    time.sleep(1)
    ksi_sub = driver.find_element_by_class_name("login100-form-btn")
    ksi_sub.click()
def logout():
    url = '/'
    ksi_logout = driver.find_element_by_xpath('//a[@href="'+url+'"]')
    ksi_logout.click()
def quit():
    driver.quit()


# In[4]:


def createUser(id_is,name_is,passwrd):
    ksi_us = driver.find_element_by_name('username')
    time.sleep(1)
    ksi_us.send_keys(id_is)
    time.sleep(1)
    ksi_name = driver.find_element_by_name('name')
    time.sleep(1)
    ksi_name.send_keys(name_is)
    time.sleep(1)
    ksi_passwrd = driver.find_element_by_name('password')
    time.sleep(1)
    ksi_passwrd.send_keys(passwrd)
    time.sleep(1)
    ksi_sub = driver.find_element_by_class_name('login100-form-btn')
    ksi_sub.click()
    


# In[5]:


driver_path = 'C:/Users/Anirudh/Downloads/chromedriver'
driver = webdriver.Chrome(options = options, executable_path = driver_path)


# In[6]:


website()


# In[7]:


createUser('PES1201700170','Anirudh Maiya','qwerty@321')


# In[26]:


quit()


# In[ ]:




