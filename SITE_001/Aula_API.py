import requests
import datetime
data = datetime.datetime.now().strftime("%d\\%m\\%Y") #strftime("%Y-%m-%d %Hh:%Mm:%Ss")
url = 'https://api.exchangerate-api.com/v6/latest'
req = requests.get(url)
# print(req.status_code)
dados = req.json()
# print(dados)
print(f"\nO valor do \"U$\":dollar hoje {data} é de R$:{dados['rates']['BRL']}")
