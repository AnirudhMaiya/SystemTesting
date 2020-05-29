#!/usr/bin/env python
# coding: utf-8

# In[21]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import numpy as np


# In[22]:


options = Options()
options.binary_location = 'C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe'


# In[23]:


def login(user_id,passwrd):
    driver.get('http://localhost:3000/')
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


# In[24]:


def courseEnrollment():
    url = '/courseenrolment'
    ksi_ce = driver.find_element_by_xpath('//a[@href="'+url+'"]')
    ksi_ce.click()

def searchCourse(which_course):
    courseEnrollment()
    time.sleep(1)
    but_choose = driver.find_element_by_xpath('//button[text()="All Courses"]')
    #but_choose.click()
    time.sleep(2)
    inp_box = driver.find_element_by_class_name("search")
    time.sleep(1)
    inp_box.send_keys(which_course)
    time.sleep(4)
    driver.switch_to.alert.accept()

def homePage():
    url = '/studentprofile'
    ksi_hp = driver.find_element_by_xpath('//a[@href="'+url+'"]')
    ksi_hp.click()


# In[25]:


driver_path = 'C:/Users/Anirudh/Downloads/chromedriver'
driver = webdriver.Chrome(options = options, executable_path = driver_path)


# In[26]:


login('PES1201700170','qwerty@321')


# In[27]:


homePage()
searchCourse('parallel compu')


# In[8]:


homePage()
searchCourse('operati')


# In[20]:


quit()


# In[ ]:




