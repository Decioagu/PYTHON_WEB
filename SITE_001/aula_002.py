# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/
# + Instalação
# - pip install requests types-requests bs4

# import re # expressões regulares
import requests
from bs4 import BeautifulSoup


url = 'http://localhost:3333/' # pagina desejada
response = requests.get(url) # obter da web
raw_html = response.content # em texto (windows)


'''
    BeautifulSoup() é uma biblioteca Python para analisar documentos HTML e XML. 
    Ele cria uma árvore de análise para páginas analisadas que podem ser usadas 
    para extrair dados de HTML:

    parsed_html = "extração de dados na web scraping"
'''
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8') # extrair (windows)

# sistema operacional MAC ou LINUX
# raw_html = response.text # em texto
# parsed_html = BeautifulSoup(raw_html, 'html.parser') # extrair 

print('===================================================================')

tag_selecionada = (parsed_html.title).text # tag

print(tag_selecionada) # . => tag do HTML

print('===================================================================')

top_jobs_heading = parsed_html.select_one('#main-header > div.main-header-content > p').text # tag

print(top_jobs_heading) # Cópia => Copiar selector | tag do HTML

print('===================================================================')

intro = parsed_html.select_one('#intro > div > div > article') # tag

if intro is not None:
    article = intro.parent
    print(article)
    print('===================================================================')

    if article is not None:
        for p in article.select('p'):
            print(p.text)
    
    # expressões regulares
    # if article is not None:
    #     for p in article.select('p'):
    #         print(re.sub(r'\s{1,}', ' ', p.text).strip())
print('===================================================================')

