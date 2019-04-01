import requests
from bs4 import BeautifulSoup
r = requests.get('http://ldf.fi/warsa/data?graph=http://ldf.fi/warsa/places/karelian_places')
soup = BeautifulSoup(r.text, 'lxml')
pattern = soup.find_all('date.begin', 'date.end')
for item in pattern:
    print(item.string)
