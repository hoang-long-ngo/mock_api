import requests

host = 'http://localhost:5000'


res = requests.get(f'{host}/adminconfig/v2/indexes')
res.raise_for_status()
print(res.text)