#!/usr/bin/env python
# coding: utf-8

# In[136]:


import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from requests import get


# In[79]:


lista_noticias = []
url = 'https://g1.globo.com/'


# In[80]:


response = requests.get(url)
response


# In[81]:


content = response.content
#armazenando conteúdo html que veio da página do G1


# In[82]:


site = bs(content, 'html.parser')


# In[83]:


print(site.prettify()) #visualizando html de melhor maneira


# In[85]:


#html da notícia
noticias = site.find_all('div', attrs={'class': 'feed-post-body'})
print(type(noticias))


# In[142]:


for noticia in noticias:
    #Titulo
    titulo = noticia.find('a', attrs = {'class': 'feed-post-link'})
    print(titulo.text)
    print(titulo['href']) #Links das notícias
    
    #Subtitulo
    subtitle = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    
    
    if(subtitle):
        print(subtitle.text)
        lista_noticias.append([titulo.text, subtitle.text, titulo['href']])
    else:
        lista_noticias.append([titulo.text,'', titulo['href']])
    
      
    
    news = pd.DataFrame(lista_noticias, columns = ['Title', 'Sub-Title', 'Link'])
    
    news.to_csv('Noticias.csv', index = False)
    
    #print(news)
    
    
    


# In[143]:


news = news.drop_duplicates()
news


# In[ ]:




