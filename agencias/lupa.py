from bs4 import BeautifulSoup
from numpy import column_stack
import requests
import pandas as pd

lista_noticias = []
response = requests.get('https://piaui.folha.uol.com.br/lupa/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

noticias = site.findAll('h2', attrs={'class' : 'bloco-title'})

for noticia in noticias:

    titulo = noticia.find('a')
    
    lista_noticias.append([titulo.text, titulo['href']])


resultado = pd.DataFrame(lista_noticias, columns=['Título', 'Link'])

resultado.to_excel('Agência Lupa.xlsx', index=False)