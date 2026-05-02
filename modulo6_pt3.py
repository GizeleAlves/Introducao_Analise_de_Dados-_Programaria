# -*- coding: utf-8 -*-
"""
Vizualização de Dados em Python
"""
# %% Módulo 6.3 Parte 1

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

import plotly.express as px

#essas duas linhas configuram para o plotly abrir no navegador
import plotly.io as pio
pio.renderers.default = 'browser'

dados = pd.read_csv('C:/Users/gizel/OneDrive/Desktop/Programaria/analise_dados.csv')

dados.head()

genero_counts = dados['GENERO'].value_counts()
# %% Vizualização de Dados em Python - Parte 1

# %%Gráfico de Barras com matplotlib 

plt.figure()
plt.bar(height=genero_counts.values, x = genero_counts.index)
plt.title('Quantidade de pessoas por gênero na área de dados')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()

# %% Gráfico de Barras com seaborn

plt.figure()
sns.countplot(data=dados, x= 'GENERO', palette='pastel')
plt.title('Quantidade de pessoas por gênero na área de Dados')
plt.xlabel("Gênero")
plt.ylabel('Contagem')
plt.grid(True)
plt.show()

# %% Vizualização de Dados em Python - Parte 2
# %% Média de salários por idade

salario_por_idade = dados.groupby('IDADE')['SALARIO'].mean()

plt.figure()
plt.plot(salario_por_idade.index, salario_por_idade.values, marker='o', linestyle='--')
plt.xlabel('Idade')
plt.ylabel('Média de salário')
plt.title('Média de salário por idade')
plt.grid(True)
plt.show()

# %% Média de salários por idade usando a biblioteca plotly

fig = px.line(salario_por_idade.reset_index( ), x='IDADE', y='SALARIO', title='Média de salário por idade', markers=True )
fig.show()
# %% Gráfico de dispersão - Média de salário por idade

plt.figure(figsize=(15,5)) #tamanho da imagem em polegadas
plt.scatter(dados['IDADE'],dados['SALARIO'], alpha=0.5) #o alpha configura a transparência dos pontinhos
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.title('Dispersão de salário por idade')
plt.grid(True)
plt.show()