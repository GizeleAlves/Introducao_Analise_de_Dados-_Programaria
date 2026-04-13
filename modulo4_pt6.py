# -*- coding: utf-8 -*-
"""
Módulo 4 - Estatística Básica Parte 6
"""
# %% Correlação, diferentes funções para dados discretos e contínuos

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

dados = pd.read_excel("planilha_modulo3.xlsx")
dados2 = pd.read_excel("Planilha_Aula_parte2.xlsx")
# %%  Correlação entre variáveis numéricas

correlacao_continua = dados['IDADE'].corr(dados['SALARIO']) #Verificando se exite correlação entre a idade e o salário
# %% Correlação entre variáveis categóricas

#Normalização de 0 a 1 das variáveis com o coeficiente de cramer

def cramer_coeficiente(coluna1, coluna2):    
    tabela_cruzada = np.array(pd.crosstab(coluna1, coluna2)) #Tabela com a quantidade de vezes que as variaveis se encontr am, sem o cabeçalho
    chi2 = chi2_contingency(tabela_cruzada)[0] #Calculando o qui quadrado, o 0 retorna só o primeiro resultado
    soma = np.sum(tabela_cruzada)
    mini = min(tabela_cruzada.shape)- 1
    cramer = np.sqrt(chi2/(soma*mini))
    return cramer

cramer_coeficiente(dados['COR/RACA/ETNIA'], dados['NIVEL DE ENSINO']) #Verificando se existe e qual a correlação entre a escolaridade e a etnia
  
#Este resultado sugere que, na nossa amostra, etnias diferentes têm níveis de ensino semelhantes, possivelmente devido ao contexto da área de TI, onde a maioria já tem algum tipo de formação.
