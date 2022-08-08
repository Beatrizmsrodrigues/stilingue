import os

import csv

import time

import pandas as pd

from pandas import json_normalize

import json

import pyodbc

from pip._vendor import requests

from datetime import date

url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios/'

request = requests.get(url=url)

obj = json.loads(request.content)

df = json_normalize(obj)

df.to_csv('streaming.csv', index=False)

data = pd.read_csv (r'streaming.csv')
df = pd.DataFrame(data)

server = '34.122.149.99'
db = ''
user = ''
password = ''

# Connect to SQL Server
conn = pyodbc.connect('Driver={SQL Server};server=34.122.149.99;Database=stilingue;IntegratedSecurity=false;UID:sqlserver;PWD:_=d|6sK:z))#~m{y;Trusted_Connection=NO')
 cursor = conn.cursor()

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dbo.regioes (id_municipio, municipio,id_uf ,sigla_uf ,nome_uf, id_regiao ,regiao_nome)
                VALUES (?,?,?,?,?,?,?)
                ''',
                row.id,
                row.nome,
                row.regiao-imediata.regiao-intermediaria.UF.id,
                row.regiao-imediata.regiao-intermediaria.UF.sigla,
                row.regiao-imediata.regiao-intermediaria.UF.nome,
                row.regiao-imediata.regiao-intermediaria.UF.regiao.id,
                row.regiao-imediata.regiao-intermediaria.UF.regiao.nome
                )
conn.commit()