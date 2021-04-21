#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
url = 'http://www.practiceselenium.com/'

driver = webdriver.Chrome()

driver.get(url)


button = driver.find_element_by_xpath('//*[@id="wsb-button-00000000-0000-0000-0000-000450914890"]')
button.click()

titulo1 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000453230000"]/div/p/span/span/strong')
titulo2 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000453231072"]/div/p/span/span/strong')
titulo3 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000453231735"]/div/p/span/span/strong')

desc1 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000451934628"]/div/pre/span')
desc2 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000451941184"]/div/pre/span[1]')
desc3 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000451944022"]/div/pre/span')

print(f'1- {titulo1.text} \n {desc1.text}' )
print(f'2- {titulo2.text} \n {desc2.text}')
print(f'3- {titulo3.text} \n {desc3.text}')

