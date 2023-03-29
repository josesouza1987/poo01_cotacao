import sys
import requests
import json
import pandas as pd


if sys.argv[1] == 'cotacao': 
    cotacoes = requests.get('https://economia.awesomeapi.com.br/json/daily/USD-BRL/30')
    cotacoes = cotacoes.json()
    df = pd.DataFrame.from_dict(cotacoes)

    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    df['dia'] = df['timestamp'].dt.day
    df['mes'] = df['timestamp'].dt.month
    df['ano'] = df['timestamp'].dt.year

    print(df.fillna(method="ffill"))

if sys.argv[2] == 'xxx': 
    print('XXX')