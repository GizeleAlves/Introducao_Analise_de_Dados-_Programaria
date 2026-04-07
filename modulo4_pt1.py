# -*- coding: utf-8 -*-
"""
Módulo 4 - Estátistica Básica

"""
# %%
import numpy as np
import pandas as pd


lista_idades = [26, 30, 32, 22, 26, 35, 40, 20, 43, 31, 23, 100]

np.sum(lista_idades) #soma dos valores das idades

len(lista_idades) #quantidade de elementos na lista

media = np.mean(lista_idades) #média das idades

lista_idades.sort() #ordenando a lista em ordem crescente

mediana = np.median(lista_idades) #mediana das idades

# %% 
"""
Aplicando estatística em um dataframe

"""

dados = pd.read_excel("planilha_modulo3.xlsx")

dados['IDADE'].mean() #Média da coluna "Idade"

dados['IDADE'].median() #Mediana da coluna "Idade"

dados['IDADE'].mode() #Moda da coluna "Idade" (Número que mais se repete)

dados['IDADE'].std() #Desvio padrão da coluna "Idade"

dados['IDADE'].min() #Idade mínima

dados['IDADE'].max() #Idade máxima
# %%
#Média de Idade do Sexo feminino

dados[dados['GENERO']=='Feminino']['IDADE'].mean()

#Média de Idade do Sexo masculino

dados[dados['GENERO']=='Masculino']['IDADE'].mean()
# %%

#Média de Salário por sexo

#Média de Salário do Sexo feminino

dados[dados['GENERO']=='Feminino']['SALARIO'].mean()

#Média de Salário do Sexo masculino

dados[dados['GENERO']=='Masculino']['SALARIO'].mean()
# %%

