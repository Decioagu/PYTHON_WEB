# Tutorial -> https://youtu.be/Qd8JT0bnJGs (aula 311)
'''
    Requests é uma biblioteca Python que fornece uma interface simples e elegante 
    para fazer solicitações HTTP. Ela é muito popular entre desenvolvedores web e de 
    APIs, pois permite enviar e receber dados de servidores HTTP de forma rápida e fácil.
'''

# requests para requisições HTTP
import requests

url = 'http://localhost:3333/' # pagina desejada
response = requests.get(url) # obter da web

print(f'{response.status_code=}') # status de resposta
print('===================================================================')
print(f'{response.headers=}') # cabeçalho 
print('===================================================================')
# print(f'{response.content=}') # conteúdo em bets
print('===================================================================')
# print(response.json()) # conteúdo em JSON - OBS: NÃO há em: url = 'http://localhost:3333/'
print('===================================================================')
print(response.text) # conteúdo em texto
