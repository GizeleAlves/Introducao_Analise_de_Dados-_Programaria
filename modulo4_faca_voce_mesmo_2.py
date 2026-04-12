# -*- coding: utf-8 -*-
"""
Módulo 4 - Faça Você Mesmo 2 - Featuring engineerring
"""
# %%
"""
Com base no que aprendemos nas aulas de Featuring engineering, crie uma nova coluna de
 Etnia - brancas, não branca e outras
"""
# %%
import pandas as pd

dados = pd.read_excel("planilha_modulo3.xlsx")

dados.columns

dados['COR/RACA/ETNIA'].value_counts()
# %%
#Função para verificar a cor e retornar uma das três categorias definidas na questão
def determinar_etnia (cor):
    if cor =='Branca':
        return 'Branca'
    elif cor=='Prefiro não informar':
        return 'Outras'
    elif cor =='Outra':
        return 'Outras'
    else:
        return 'Não brancas'
    
#Usando a função apply para criar uma nova coluna e preenche-la utilizando a função definida anteriormente

dados['ETNIA'] = dados['COR/RACA/ETNIA'].apply(determinar_etnia)

dados['ETNIA'].value_counts()

dados['COR/RACA/ETNIA'].value_counts()
