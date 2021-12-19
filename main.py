from flask import Flask, jsonify # Jsonify transforma um dict Python em formato json
import pandas as pd # Importanto o Pandas com o nome de "pd"

# Iniciando API
app = Flask(__name__) # Formato padrão de inicialização do Flask


# Construindo funcionalidade
"""
A diferença de um site para uma API na construção, é que ao invés de a API dar como resposta um site, ele dá
como resposta um "json"
"""
@app.route('/')
def homepage():
    return 'A API está funcionando!'

@app.route('/pegar_vendas') # Link
def pegar_vendas():
    tabela = pd.read_csv('Base de dados/Base de dados.csv') # Importado a base de dados na variável "tabela"
    total_vendas = tabela['Vendas'].sum() # Somando o tatal de vendas da tabela da base de dados
    resposta = {'total_vendas': total_vendas} # Dicionário com o total de vendas
    return  jsonify(resposta) # Retorna as informações da 'var resposta' em formato json
"""
Numa API, o link se torna um "endpoint da API", que é quando o link retorna uma informação da API para o usuário
"""
app.run() # inicia a API