# -*- coding: utf-8 -*-
"""
Módulo 4 - Faça Você Mesmo 1 - Tratando valores faltantes
"""
# %%

"""
Utilizando a planilha licitacoes.csv

> Identifique qual coluna possui valores faltantes

> Identifique o tipo de dados desta coluna

> Substitua os valores faltantes pelo mesmo formato 

*com a possibilidade de substituir por datas inexistentes.
"""
# %%
import numpy as np
import pandas as pd

dados = pd.read_csv('licitacoes.csv', encoding="latin1", sep=";")
# %%
dados.info()

#Verifica-se que data abertura é quem tem valores nulos

dados['Data Abertura'].isnull().value_counts() #Temos 10648 valores nulos na coluna "Data Abertura"

# vamos substituir os valores nulos por uma data inexistente "01/01/1900"

dados.loc[dados['Data Abertura'].isnull(),'Data Abertura'] = '01/01/1900'
# %%
dados = pd.read_csv('licitacoes.csv', encoding="latin1", sep=";")

dados['Data Abertura'] = dados['Data Abertura'].fillna('01/01/1900')
# %% Também podemos substituir pela moda das datas

dados.loc[dados['Data Abertura'].isnull(),'Data Abertura'] = dados['Data Abertura'].mode()





