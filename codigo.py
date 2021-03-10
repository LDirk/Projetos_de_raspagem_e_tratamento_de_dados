import pandas as pd  
import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.terra.com.br/esportes/futebol/brasileiro-serie-a/tabela/")

if req.status_code == 200:
  print("A requesição foi um sucesso")

  # Content para acessar o código da página HTML. 
  content = req.content
 
soup = BeautifulSoup(content, 'html.parser')
table = soup.find_all(name='table') 

table_str = str(table)
df = pd.read_html(table_str)[0]


#Ajeitando o dataSet
colsToDrop = ['Times.1', "Times.3", "%"]
df = df.drop(colsToDrop, axis=1)

df = df.rename(columns={'Times': 'Classificação'})
df = df.rename(columns={'Times.2': 'Times'})
df = df.rename(columns={'P': 'Pontos'})
df = df.rename(columns={'J': 'Jogos'})
df = df.rename(columns={'V': 'Vitorias'})
df = df.rename(columns={'E': 'Empates'})
df = df.rename(columns={'D': 'Derrotas'})
df = df.rename(columns={'GP': 'Gols Pro'})
df = df.rename(columns={'GC': 'Gols Contra'})
df = df.rename(columns={'SG': 'Saldo de Gols'})


print(df)

df.to_csv('file.csv')
