# -*- coding: utf-8 -*-
"""
Conectando SQL com o Pandas
# %%
"""
# %% Módulo 5.6 - Part 1
import sqlite3
import pandas as pd

conexao = sqlite3.connect('C:/Users/gizel/OneDrive/Desktop/Programaria/status_brasil')

query = "SELECT * FROM Municipios_Brasileiros WHERE Cidade = 'Itaquaquecetuba';"

pd.read_sql(query,con=conexao)
# %% Módulo 5.6 Part 2

#Vendo a média da renda por estado

query = '''SELECT Municipios_Brasileiros.Estado, AVG(Municipio_Status.renda) FROM  Municipios_Brasileiros 
INNER JOIN Municipio_Status ON Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID
GROUP BY Municipios_Brasileiros.Estado'''

pd.read_sql(query,con=conexao)
# %% Juntar com o csv que salvamos nas aulas anteriores

dados = pd.read_csv('C:/Users/gizel/OneDrive/Desktop/Programaria/analise_dados.csv')

dados.columns

lista_estados = list(dados['UF ONDE MORA'].unique()) #Pegando os estados do csv



# %% Formatando a query para pegar a média de renda somente dos estados que constam na lista_estados

query = '''SELECT Municipios_Brasileiros.Estado, AVG(Municipio_Status.renda) FROM  Municipios_Brasileiros 
INNER JOIN Municipio_Status ON Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID
WHERE Municipios_Brasileiros.Estado IN ({})
GROUP BY Municipios_Brasileiros.Estado '''.format(','.join(['?' for _ in lista_estados]))

#Salva a média e os estados em um dataframe
estados_renda = pd.read_sql(query,con=conexao, params=lista_estados)

#Renommeando a coluna para "UF ONDE MORA" para "Estado"

dados.rename(columns={'UF ONDE MORA': 'Estado'},inplace = True)

dados.columns

#juntando a tabela dados com a tabela estados_renda pela coluna "Estado"

dados = dados.merge(estados_renda, on="Estado",how='left')
# %% Calculando a correlação entre renda e salário

correlacao_renda_salario = dados['SALARIO'].corr(dados['AVG(Municipio_Status.renda)'])



