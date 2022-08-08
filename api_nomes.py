import pandas as pd
import json
from pandas import json_normalize
from pip._vendor import requests
from datetime import date


url = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking'

request = requests.get(url=url)

obj_nomes = json.loads(request.content)

df = json_normalize(obj_nomes)

df.to_csv('nomes.csv', index=False)

data = pd.read_csv (r'nomes.csv')
df = pd.DataFrame(data)
