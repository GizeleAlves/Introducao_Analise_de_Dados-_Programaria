# -*- coding: utf-8 -*-
"""
Módulo 5 - Faça Você Mesmo 2 - Correlação

"""
# %%

'''Faça a mesma análise da aula anterior utilizando o índice 
de educação. Existe alguma correlação com salário?'''
# %%

import sqlite3
import pandas as pd

conexao = sqlite3.connect('C:/Users/gizel/OneDrive/Desktop/Programaria/status_brasil')

dados = pd.read_csv('C:/Users/gizel/OneDrive/Desktop/Programaria/analise_dados.csv')

# %%

#Vendo a média do índice de eduação por estado

consulta = '''SELECT Municipios_Brasileiros.Estado, AVG(Municipio_Status.educacao) FROM  Municipios_Brasileiros 
INNER JOIN Municipio_Status ON Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID
GROUP BY Municipios_Brasileiros.Estado'''

pd.read_sql(consulta,con=conexao)
# %% Pegando os estados da tabela e salvando em uma lista

lista_estados = list(dados['UF ONDE MORA'].unique()) #Pegando os estados do csv

dados.rename(columns={'UF ONDE MORA': 'Estado'},inplace = True) #Renommeando a coluna para "UF ONDE MORA" para "Estado"

# %% Formatando a query para pegar a média de renda somente dos estados que constam na lista_estados

consulta = '''SELECT Municipios_Brasileiros.Estado, AVG(Municipio_Status.educacao) FROM  Municipios_Brasileiros 
INNER JOIN Municipio_Status ON Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID
WHERE Municipios_Brasileiros.Estado IN ({})
GROUP BY Municipios_Brasileiros.Estado '''.format(','.join(['?' for _ in lista_estados]))

#Salva a média e os estados em um dataframe
estados_educacao = pd.read_sql(consulta,con=conexao, params=lista_estados)
# %%

#juntando a tabela dados com a tabela estados_educacao pela coluna "Estado"

dados = dados.merge(estados_educacao, on="Estado",how='left')

#Renommeando a nova coluna para "Indíce Educação"

dados.rename(columns={'AVG(Municipio_Status.educacao)': 'Indice Educacao'},inplace = True)

#Calculando a correlação entre educação e salário

correlacao_educacao_salario = dados['SALARIO'].corr(dados['Indice Educacao'])

