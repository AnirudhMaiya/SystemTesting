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

def searchCourse(which_course):
    courseEnrollment()
    time.sleep(1)
    but_choose = driver.find_element_by_xpath('//button[text()="All Courses"]')
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


# In[5]:


driver_path = 'C:/Users/Anirudh/Downloads/chromedriver'
driver = webdriver.Chrome(options = options, executable_path = driver_path)


# In[6]:


login('PES1201700170','qwerty@321')


# In[7]:


def choose_course_review():
    url = '/coursereview'
    ksi_ce = driver.find_element_by_xpath('//a[@href="'+url+'"]')
    ksi_ce.click()

def update_table(mrks,row_is):
    ass = row_is.find_elements_by_tag_name("td")[3]
    ee = ass.find_element_by_name("marks")
    time.sleep(1)
    ee.send_keys(mrks)
    ff = ass.find_element_by_class_name('login2-form-btn')
    ff.click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    
def out_table():
    tab_name = driver.find_element_by_xpath("//table[@class='zebra review_table']")
    rows = tab_name.find_elements_by_xpath(".//tr")
    for i in range(len(rows)):
        time.sleep(2)
        dub_name = driver.find_element_by_xpath("//table[@class='zebra review_table']")
        dub_row = dub_name.find_elements_by_xpath(".//tr")
        what_is_my_marks = np.random.randint(1,10)
        print(dub_row[i],what_is_my_marks)
        update_table(what_is_my_marks,dub_row[i])


# In[8]:


choose_course_review()
time.sleep(2)
out_table()


# In[ ]:




