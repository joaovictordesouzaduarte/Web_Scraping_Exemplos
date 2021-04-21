#!/usr/bin/env python
# coding: utf-8

# In[ ]:

#Importamos bibliotecas
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#Pegamos a url
url = 'http://www.practiceselenium.com/'


#damos um get na url;
driver = webdriver.Chrome()

driver.get(url)

#Neste código, faremos o Python "clicar" no botão em questão o "See Collection"
button = driver.find_element_by_xpath('//*[@id="wsb-button-00000000-0000-0000-0000-000450914890"]')
button.click()


#Abrindo o "See Collection", pegamos os títulos de cada chá;
titulo1 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000453230000"]/div/p/span/span/strong')
titulo2 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000453231072"]/div/p/span/span/strong')
titulo3 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000453231735"]/div/p/span/span/strong')

#Agora, pegamos a descrição de cada chá;
desc1 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000451934628"]/div/pre/span')
desc2 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000451941184"]/div/pre/span[1]')
desc3 = driver.find_element_by_xpath('//*[@id="wsb-element-00000000-0000-0000-0000-000451944022"]/div/pre/span')


#Printamos os resultados;
print(f'1- {titulo1.text} \n {desc1.text}' )
print(f'2- {titulo2.text} \n {desc2.text}')
print(f'3- {titulo3.text} \n {desc3.text}')

