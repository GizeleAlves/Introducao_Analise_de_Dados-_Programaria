# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 13:24:37 2026

@author: gizel

Python para análise de Dados

"""

# %%Importando o pandas e carregando a planilha

import pandas as pd

dados = pd.read_excel("planilha_modulo3.xlsx")
# %% Informações sobre a tabela

dados.head(10)  #primeiras linhas

dados.tail(7) #últimas linhas

dados.shape #tamanho da tabela

len(dados) #tamanho da tabela

dados.columns# colunas da tabela

dados.info()

dados.describe()
# %% Gênero Feminino

dados.columns
dados['GENERO']
dados[dados['GENERO']=='Feminino']


#pega todas as linhas que na coluna GENERO tenha a palavra não

dados[dados['GENERO'].str.contains('não',na=False)]
# %%  Filtro por idade

dados[dados['IDADE']>30]
# %% Combinando filtros

dados[(dados['IDADE']>30) & (dados['GENERO']=='Feminino')]
# %% Agrupamentos e contagens

dados['FAIXA IDADE'].nunique() #conta quantas faixas de idadde existem

dados.groupby('GENERO')['ID'].nunique() #Agrupa, e conta quantas pessoas existem por gênero

dados.groupby('GENERO', dropna = False)['ID'].nunique() #AMesmo do anterior, mas mostrando os nulos

dados['NIVEL DE ENSINO'].value_counts() # Quantas pessoas por nível de ensino

dados['GENERO'].value_counts(dropna=False) #Quantas pessoas por gênero, incluindo os nulos

dados['REGIAO ONDE MORA'].value_counts()

dados[dados['IDADE']>30]['NIVEL'].value_counts() #Idade das pessoas 30+ por nível de escolaridade


dados[(dados['IDADE']>30) & (dados['GENERO'] == 'Feminino')]['NIVEL'].value_counts() #Idade das pessoas 30+ por nível de escolaridade e gênero feminino

# %%  Faça você mesmo

#Pessoas que se declaram amarelas e abaixo de 40 anos

amarelas = dados[dados['COR/RACA/ETNIA'] == "Amarela"]
quarentaMenos = dados[dados['IDADE']<40]

amarelasMenos40 = dados[(dados['COR/RACA/ETNIA'] == 'Amarela') & (dados['IDADE']<40)] 

# %% TABELA DINÂMICA - PIVOT TABLE

tabela_dinamica=pd.pivot_table(dados, values=['ID'], index=['GENERO'], columns=['GESTOR?'], aggfunc='count')
      



