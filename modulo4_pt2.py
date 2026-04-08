# -*- coding: utf-8 -*-
"""
Módulo 4 - Estátistica Básica Parte 1

"""
# %%
#Tratando os nulos

import numpy as np
import pandas as pd

dados = pd.read_excel("planilha_modulo3.xlsx")
# %%  Coluna de Gênero - Substituindo os nulos por um valor da planilha

dados.groupby('GENERO', dropna=False)['ID'].nunique() #Agrupar os únicos por gênero, incluindo os valores nulos

dados['GENERO'].fillna("Prefiro não informar") 
dados['GENERO']=dados['GENERO'].fillna("Prefiro não informar") #Substituir os valores nulos

# %%  Coluna de Idade

dados['IDADE'].isnull().value_counts() #Mostra "True" quando um dado é nulo

dados[dados['IDADE'].isnull()]['FAIXA IDADE'].value_counts() #Conferindo dentre os valores nulos de "IDADE", quais preencheram a "Faixa Idade

#Primeiro, vamos tratar os campos com "Idade" nula, na faixa de 17-21 anos

media_17_21 = dados[dados['FAIXA IDADE']=='17-21']['IDADE'].mean() #Descobrindo a média de idade para essa faixa de idade

#Localizar as linhas e conlunas das células que estão nulas e que têm a faixa de idade entre 17 e 21 anos e atribuindo a média a essas células

dados.loc[(dados['FAIXA IDADE']=='17-21')&(dados['IDADE'].isnull()), 'IDADE'] = media_17_21

#Agora vamos tentar fazer o mesmo para a faixa de idade 55+

dados[dados['FAIXA IDADE']=='55+']['IDADE'] #Ao executar percebemos que nenhuma das pessoas de 55+ preencheram a coluna idade

dados[dados['FAIXA IDADE']=='55+']['NIVEL'] #Verificar essa faixa de idade por nível

#Como não podemos inferir qual a idade dessas pessoas, vamos substituir os nulos pela média geral da coluna idade

media_geral = dados['IDADE'].mean() #calculando a média de idade

#Localizar as linhas e conlunas das células que estão nulas e que têm a faixa de idade 55+ anos e atribuindo a média geral a essas células

dados.loc[(dados['FAIXA IDADE']=='55+')&(dados['IDADE'].isnull()),'IDADE'] = media_geral
# %%  Coluna Salário

dados[dados['SALARIO'].isnull()] #Verificando quantas linhas da tabela tem a célula sálario nula (577)

#Verificando quantos salários nulos tem, pela faixa salarial

dados[dados['SALARIO'].isnull()]['FAIXA SALARIAL'].value_counts() 

#O resultado significa que quem não preencheu o salário,também não preencheu a faixa salarial. Dessa forma, vamos substituir os nulos pela mediana, que é menos influenciável por valores discrepantes que a média

mediana_salario = dados['SALARIO'].median()

#Localizar as linhas e colunas das células que estão nulas na coluna salário e susbstituir pela mediana do salário

dados.loc[dados['SALARIO'].isnull(),'SALARIO'] = mediana_salario








