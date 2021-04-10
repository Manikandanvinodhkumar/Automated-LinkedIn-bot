# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:14:08 2021

@author: manik
"""
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 20:52:02 2021

@author: manik
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui as pag

#from random import randint
from numpy.random import rand
from numpy.random import randint
import numpy as np

import time
import codecs
#url = 'https://twitter.com/SHAQ'
#url2 = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&industry=%5B%2296%22%2C%2243%22%2C%224%22%2C%226%22%5D&keywords=data%20analyst&origin=FACETED_SEARCH&profileLanguage=%5B%22en%22%5D'
url2 = 'https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=data%20analyst&origin=FACETED_SEARCH&page=5&profileLanguage=%5B%22en%22%5D&serviceCategory=%5B%22220%22%2C%22602%22%2C%222461%22%2C%2263%22%5D'

# open the browser and visit the url
url =  "http://linkedin.com/"
driver = webdriver.Chrome('./chromedriver/chromedriver')
time.sleep(1)
driver.get(url)
time.sleep(1)

#login and searh for data analyst
username = driver.find_element_by_id("session_key")
username.send_keys("mvinodhk@stevens.edu")
password = driver.find_element_by_id("session_password")
password.send_keys("ilikemyMOM!")
driver.find_element_by_class_name("sign-in-form__submit-button").click()

driver.get(url2)


#driver.current_url
pgs = driver.find_element_by_css_selector('li[class="artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view"]')

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#wait = WebDriverWait(driver, 10)
    
for i in range(1,100,1):
    driver.execute_script("scrollBy(0,250);")
    time.sleep(10)
    items = driver.find_elements_by_css_selector('div[class= "entity-result__actions entity-result__divider"]')
    for item in items:
        print(item.text)
        time.sleep(2)
        try:
            item.find_element_by_class_name("artdeco-button__text").click()
            f1 = driver.find_element_by_css_selector('div[class="artdeco-modal__actionbar text-align-right ember-view"]')
            f3 = f1.find_element_by_css_selector('button[class= "mr1 artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--secondary ember-view"]')
            f3.click()
            f4 = driver.find_element_by_css_selector('textarea[class="ember-text-area ember-view connect-button-send-invite__custom-message mb3"]')
            f4.send_keys('''Hi,
                     This is Manikandan with Master's degree in Business Intelligence and Analytics at Stevens Institute of Technology. I happen to have a background and exposure in Data Analytics. I'd love to connect  up and learn more about your work as a Data Analyst at your company.
                     
                     Regards,
                     Manikandan''')
            f5 = f1.find_element_by_css_selector('button[class= "ml1 artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]').click()
        except:
            print('already sent') 
    print('done') 
    
    n = i
    time.sleep(10)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print('page no is {}'.format(n))
    time.sleep(30)
    pgs = driver.find_element_by_css_selector('ul[class="artdeco-pagination__pages artdeco-pagination__pages--number"]')
    print('its working fine')
    #time.sleep(10)
    try:
        pg_select = pgs.find_element_by_css_selector('button[aria-label= "Page {}"]'.format(n))
        print('test 2')
    except:
        pg_select = pgs.find_element_by_css_selector('button[aria-label= "Page {}"]'.format(n-1))
        print('test 2')   
    pg_select.click()
    print(n)

