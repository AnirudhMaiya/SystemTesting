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


# In[4]:


def courseEnrollment():
    url = '/courseenrolment'
    ksi_ce = driver.find_element_by_xpath('//a[@href="'+url+'"]')
    ksi_ce.click()

def chooseRec():
    courseEnrollment()
    time.sleep(2)
    but_choose = driver.find_element_by_xpath('//button[text()="Reccomended"]')
    but_choose.click()
    time.sleep(2)
    ksi_choose_rec_course = driver.find_element_by_class_name('proceed_to_enroll')
    ksi_choose_rec_course.click()
    time.sleep(4)
    driver.switch_to.alert.accept()
    
def homePage():
    url = '/studentprofile'
    ksi_hp = driver.find_element_by_xpath('//a[@href="'+url+'"]')
    ksi_hp.click()


# In[5]:


def clickCourse():
    url = '/createcourse'
    ksi_cc = driver.find_element_by_xpath('//a[@href="'+url+'"]')
    ksi_cc.click()


# In[6]:


def addCourse(crsid,crsname,crsdesc):
    ksi_ci = driver.find_element_by_name('courseid')
    time.sleep(1)
    ksi_ci.send_keys(crsid)
    time.sleep(1)
    ksi_name = driver.find_element_by_name('name')
    time.sleep(1)
    ksi_name.send_keys(crsname)
    time.sleep(1)
    ksi_desc = driver.find_element_by_xpath('//*[@id="root"]/div/div/div[2]/div/div/form/div[3]/input')
    time.sleep(1)
    ksi_desc.send_keys(crsdesc)
    time.sleep(1)
    ksi_sub = driver.find_element_by_class_name('login100-form-btn')
    ksi_sub.click()
    


# In[7]:


driver_path = 'C:/Users/Anirudh/Downloads/chromedriver'
driver = webdriver.Chrome(options = options, executable_path = driver_path)


# In[8]:


login('PES1201700170','qwerty@321')


# In[9]:


time.sleep(2)
clickCourse()
time.sleep(1)


# In[10]:


addCourse('UE17CS02','Java','Learn OOPsssssssss')


# In[ ]:




