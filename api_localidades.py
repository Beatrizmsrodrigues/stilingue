import pandas as pd
import json
from pandas import json_normalize
from pip._vendor import requests

url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios/'

request = requests.get(url=url)

obj_localidades = json.loads(request.content)

df = json_normalize(obj_localidades)

df.to_csv('localidades.csv', index=False)

data = pd.read_csv (r'localidades.csv')
df = pd.DataFrame(data)


