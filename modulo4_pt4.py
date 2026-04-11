# -*- coding: utf-8 -*-
"""
Módulo 4 - Estatística Básica Parte 4

"""
# %% Intervalo de confiança e distribuição amostral

import numpy as np
import pandas as pd
from scipy import stats #funções de estatística 

dados = pd.read_excel("planilha_modulo3.xlsx")

#Repetindo todos os tratamentos já feitos para a coluna salário na parte 3 do módulo 4

q1 = dados['SALARIO'].quantile(0.25) #primeiro quartil

q3 = dados['SALARIO'].quantile(0.75) #terceiro quartil


iqr = q3 - q1 #valor interquartil

lim_superior = q3 + (1.5 * iqr) #barrinha superior do gráfico boxplot

lim_inferior = q1 - (1.5 * iqr) #barrinha superior do gráfico boxplot

dados['FAIXA SALARIAL'].value_counts() #Observando a quantidade de pessoas para cada faixa salarial

media_salario = dados['SALARIO'].mean()

desvio_salario = dados['SALARIO'].std()

limite_superior =  media_salario +(3*desvio_salario) #Qualquer valor acima desse, é considerado outlier

dados[dados['SALARIO']>limite_superior]['FAIXA SALARIAL'].value_counts() #verificando os outliers por faixa salarial

#Vamos substituir os outliers pela média de salário que estão na mesma faixa salarial

#Primerio calculamos a média de cada faixa, excluindo os valores que estão acima do limite superior
media_30_40 = dados[(dados['FAIXA SALARIAL']=='de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']<limite_superior)]['SALARIO'].mean()

media_40 = dados[(dados['FAIXA SALARIAL']=='Acima de R$ 40.001/mês') & (dados['SALARIO']<limite_superior)]['SALARIO'].mean()

#Localizar esse otliers e substituir pela média

dados.loc[(dados['FAIXA SALARIAL']=='de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']>limite_superior), 'SALARIO'] = media_30_40

dados.loc[(dados['FAIXA SALARIAL']=='Acima de R$ 40.001/mês') & (dados['SALARIO']>limite_superior),'SALARIO'] = media_40
# %% A parte 4 do Módulo 4 começa aqui - Distribuição amostral e intervalo de confiança

salarios = dados['SALARIO']

media_amostral = np.mean(salarios) #Média da amostra

desvio_amostral = np.std(salarios) #Desvio padrão da amostra

nivel_confianca = 0.95

tamanho_amostra = len(salarios)

erro_padrão = stats.sem(salarios)

intervalo_confianca = stats.t.interval(nivel_confianca, tamanho_amostra-1, loc=media_amostral, scale=erro_padrão)

# Esse resultado significa que com os dados disponíveis, temos 95% de confiança que a média salaria de pessoas de dados no Brasil fica entre os valores demonstrados nesse intervalo
