# -*- coding: utf-8 -*-
"""
Módulo 4 - Estatística Básica Parte 3

"""
# %%  Valores discrepantes (outliers)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


lista_idades = [26, 30, 32, 22, 26, 35, 400, 20, 43, 31, 23]

media = np.mean(lista_idades)

desvio = np.std(lista_idades) #Verificando que o desvio padrão é muito alto

limite_superior = media + 3* desvio # o que for acima desse limite superior é tudo outlier

limite_inferior = media - 3* desvio # o que for abaixo desse limite inferior é tudo outlier

plt.boxplot(lista_idades) #Gerando o boxplot das idades
# %% Voutando para a planilha anterior

dados = pd.read_excel("planilha_modulo3.xlsx")

dados[dados['SALARIO'].isnull()] #Verificando quantas linhas da tabela tem a célula sálario nula (577)

#Verificando quantos salários nulos tem, pela faixa salarial

dados[dados['SALARIO'].isnull()]['FAIXA SALARIAL'].value_counts() 

#O resultado significa que quem não preencheu o salário,também não preencheu a faixa salarial. Dessa forma, vamos substituir os nulos pela mediana, que é menos influenciável por valores discrepantes que a média

mediana_salario = dados['SALARIO'].median()

#Localizar as linhas e colunas das células que estão nulas na coluna salário e susbstituir pela mediana do salário

dados.loc[dados['SALARIO'].isnull(),'SALARIO'] = mediana_salario

plt.boxplot(dados['SALARIO']) #Vendo a dispersão dos salários, depois de tratar os nulos
# %% Cálculo dos quartis

q1 = dados['SALARIO'].quantile(0.25) #primeiro quartil

q3 = dados['SALARIO'].quantile(0.75) #terceiro quartil


iqr = q3 - q1 #valor interquartil

lim_superior = q3 + (1.5 * iqr) #barrinha superior do gráfico boxplot

lim_inferior = q1 - (1.5 * iqr) #barrinha superior do gráfico boxplot

dados['FAIXA SALARIAL'].value_counts() #Observando a quantidade de pessoas para cada faixa salarial

media_salario = dados['SALARIO'].mean()

desvio_salario = dados['SALARIO'].std()

limite_superior =  media_salario +(3*desvio_salario) #Qualquer valor acima desse, é considerado outlier
# %% Decidindo o que fazer com os outliers

dados[dados['SALARIO']>limite_superior]['FAIXA SALARIAL'].value_counts() #verificando os outliers por faixa salarial

#Vamos substituir os outliers pela média de salário que estão na mesma faixa salarial

#Primerio calculamos a média de cada faixa, excluindo os valores que estão acima do limite superior
media_30_40 = dados[(dados['FAIXA SALARIAL']=='de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']<limite_superior)]['SALARIO'].mean()

media_40 = dados[(dados['FAIXA SALARIAL']=='Acima de R$ 40.001/mês') & (dados['SALARIO']<limite_superior)]['SALARIO'].mean()

#Localizar esse otliers e substituir pela média

dados.loc[(dados['FAIXA SALARIAL']=='de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']>limite_superior), 'SALARIO'] = media_30_40

dados.loc[(dados['FAIXA SALARIAL']=='Acima de R$ 40.001/mês') & (dados['SALARIO']>limite_superior),'SALARIO'] = media_40

plt.boxplot(dados['SALARIO']) #Gerando o gráfico novamente

#Dessa vez, os pontos acima no gráfico estão abaixo do limite superior, então não podem ser considerados otliers
# %% 







