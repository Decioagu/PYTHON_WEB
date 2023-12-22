import requests as req
from datetime import datetime

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = req.get(url)
print(resp)
inf = resp.json()
print(inf)
for v in inf:
    del v['ID']
    del v['Country']
    del v['CountryCode']
    del v['Province']
    del v['City']
    del v['CityCode']
    del v['Lat']
    del v['Lon']
print(inf)
for v in inf:
    v['Date'] = datetime.strptime(v['Date'][:10], '%Y-%m-%d').date()
    print(f"{v['Date']}:{type(v['Date'])}")
inf.insert(0, {'Confirmed': 'Confirmados', 'Deaths': 'Mortos', 'Recovered': 'Recuperados', 'Active': 'Casos Ativo', 'Date': 'Data'})
for v in inf:
    print(v.values())
