# -*- coding: utf-8 -*-
"""
Módulo 4 - Faça Você Mesmo 3 - Correlação
"""
# %%
"""
Faça a correlação entre nível de ensino e gênero
"""
# %%

import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

dados = pd.read_excel("planilha_modulo3.xlsx")

dados.columns
# %%

def cramer_coeficiente(coluna1, coluna2):    
    tabela_cruzada = np.array(pd.crosstab(coluna1, coluna2))
    chi2 = chi2_contingency(tabela_cruzada)[0] 
    soma = np.sum(tabela_cruzada)
    mini = min(tabela_cruzada.shape)- 1
    cramer = np.sqrt(chi2/(soma*mini))
    return cramer

cramer_coeficiente(dados['NIVEL DE ENSINO'], dados['GENERO']) 
# %%


