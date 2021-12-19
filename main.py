from flask import Flask
import pandas as pd # Importanto o Pandas com o nome de "pd"

app = Flask(__name__) # Formato padrão de inicialização do Flask

# tabela = pd.read_csv('Base de dados/Base de dados.csv') # Importado a base de dados na variável "tabela"
# total_vendas = tabela['Vendas'].sum()
# print(total_vendas)