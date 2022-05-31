from bs4 import BeautifulSoup
import pandas as pd
import requests


lista_noticias = []

response = requests.get('https://projetocomprova.com.br/?filter=eleicoes')

content = response.content

site = BeautifulSoup(content, 'html.parser')

dates = site.findAll('span', attrs={'class' : 'answer__credits__date'})
titles = site.findAll('h1', attrs={'class' : 'answer__title'})
links = site.findAll('a', attrs={'class': 'answer__title__link'})
#images = site.findAll('div', attrs={'class' : 'answer__image'})


for (data, title, links) in zip(dates, titles, links):
    
    lista_noticias.append([data.text, title.text, links['href']])
    #lista_noticias.append([data.text, title.text, links['href'], images['style']])

    
resultado = pd.DataFrame(lista_noticias, columns=['Data', 'Título', 'Link'])

resultado.to_excel('Projeto Comprova.xlsx', index=False)


