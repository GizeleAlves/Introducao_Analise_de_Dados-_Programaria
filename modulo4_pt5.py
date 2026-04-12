# -*- coding: utf-8 -*-
"""
Módulo 4 - Estatística Básica Parte 5
"""
# %% Featuring engineering

import numpy as np
import pandas as pd

dados = pd.read_excel("planilha_modulo3.xlsx")
# %%

#Criando uma função para tratar se a pessoa é gestora ou tem outro nível definido

def preencher_nivel(gestor, nivel): 
    if gestor == 1:
        return "Pessoa Gestora"
    else:
        return nivel

#Cria a coluna "NOVO_NIVEL" e a preenche da seguinte forma: se tiver 1 na coluna "GESTOR?" preencha com "Pessoa Gestora", se não preencha com o mesmo que está escrito na coluna "NIVEL"
    
dados['NOVO_NIVEL'] = dados.apply(lambda x: preencher_nivel(x['GESTOR?'], x['NIVEL']), axis=1)

dados['NOVO_NIVEL'].value_counts()

dados['NIVEL']

#Vamos criar uma coluna para cada nível 
dados = pd.get_dummies(dados,columns=['NIVEL'])

#Função para determinar a geração pela coluna idade

def determinar_geracao (idade):
    if 39<idade<=58:
        return "Geração X"
    elif 29 < idade <= 39:
        return "Millenial"
    elif 13 < idade <= 29:
        return "Geração Z"
    else:
        return "Outra Geração"

dados['GERACAO'] = dados['IDADE'].apply(determinar_geracao)

dados['GERACAO'].value_counts()
# %% Juntando duas planilhas

dados2 = pd.read_excel("Planilha_Aula_parte2.xlsx")

dados2.head()

dados = dados.merge(dados2, on='ID', how='left') #juntando duas planilhas

dados.columns #avaliando as colunas existentes
dados['Você pretende mudar de emprego nos próximos 6 meses?'].value_counts()

#Agora vamos criar duas colunas, uma para quem está buscando emprego, e outra para quem não está

# Verifica as respostas que tem "... em busca.." e adiciona um TRUE na coluna "EM BUSCA"

dados['EM BUSCA'] = dados['Você pretende mudar de emprego nos próximos 6 meses?'].str.contains('em busca', case=False)

dados['EM BUSCA'].value_counts()

# Verifica as respostas que tem "... aberto.." e adiciona um TRUE na coluna "ABERTO_OPORTUNIDADES"

dados['ABERTO_OPORTUNIDADES'] = dados['Você pretende mudar de emprego nos próximos 6 meses?'].str.contains('aberto', case=False)

dados['ABERTO_OPORTUNIDADES'].value_counts()
