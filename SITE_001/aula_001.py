# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443
url = 'http://localhost:3333/'
response = requests.get(url)

print(f'{response.status_code=}') # status de resposta
print('===================================================================')
print(f'{response.headers=}') # cabeçalho 
print('===================================================================')
# print(f'{response.content=}') # conteúdo em bets
print('===================================================================')
# print(response.json()) # conteúdo em JSON - OBS: NÃO há em: url = 'http://localhost:3333/'
print('===================================================================')
print(response.text) # conteúdo em texto
