"""
Módulo 7 - Introdução ao Aprendizado de Máquina
"""
# %%  Regressão Linear

import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression

from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

import matplotlib.pyplot as plt

dados = pd.read_excel('C:/Users/gizel/OneDrive/Desktop/Programaria/analise_dados_mod7_(1).xlsx')

# %%


dados['QUAL SUA SITUAÇÃO ATUAL DE TRABALHO?'].value_counts()

#Pegando apenas as linhas da planilha referentes a empregados CLT

dados = dados[dados['QUAL SUA SITUAÇÃO ATUAL DE TRABALHO?'] == 'Empregado (CLT)']

dados['COR/RACA/ETNIA'].value_counts()

#Retirar os dados das amostras que são muito pequenas (Indígena, Outra e Prefiro não informar)

lista_retirar = ['Prefiro não informar', 'Outra', 'Indígena']

dados = dados[~dados['COR/RACA/ETNIA'].isin(lista_retirar)]  #O TIL é como se fosse um NOT, ou seja, faz o contrário do que diz no comando

#criar uma coluna de não brancos, onde quando a pessoa for não branca vai ser atribuido o valor 1

dados['NAO_BRANCA'] = dados['COR/RACA/ETNIA'].apply(lambda x: 1 if x!= 'Branca' else 0)

dados['QUANTO TEMPO DE EXPERIÊNCIA NA ÁREA DE DADOS VOCÊ TEM?'].value_counts()

# Criando a coluna tempo de experiencia com apenas o primeiro número da coluna 'QUANTO TEMPO DE EXPERIÊNCIA NA ÁREA DE DADOS VOCÊ TEM?'

dados['TEMPO_EXPERIENCIA'] = dados['QUANTO TEMPO DE EXPERIÊNCIA NA ÁREA DE DADOS VOCÊ TEM?'].str.extract(r'(\d+)')

dados['TEMPO_EXPERIENCIA'].value_counts()

dados['NUMERO DE FUNCIONARIOS'].value_counts()

#Substituit o ponto dos núneros da coluna "Número de Funcionários"

dados['NUMERO DE FUNCIONARIOS'] = dados['NUMERO DE FUNCIONARIOS'].str.replace('.','')

# Criando a coluna tempo de experiencia com apenas o primeiro número da coluna 'NUMERO DE FUNCIONARIOS'

dados['NUMERO DE FUNCIONARIOS'] = dados['NUMERO DE FUNCIONARIOS'].str.extract(r'(\d+)')

# Verificando se existem nulos nas variáveis, e tratando substituindo por zero
dados['NUMERO DE FUNCIONARIOS'].value_counts(dropna = False)
dados['TEMPO_EXPERIENCIA'].value_counts(dropna = False)

dados['TEMPO_EXPERIENCIA'] = dados['TEMPO_EXPERIENCIA'].fillna(0)
# %%

dados['Qual o principal motivo da sua insatisfação com a empresa atual?'].value_counts()

#Criar uma coluna chamada insatisfação, e todas as linhas que o motivo sitar a palavra salário, vai ser atribuido o valor 1

dados['INSATISFACAO'] = 0

dados.loc[dados['Qual o principal motivo da sua insatisfação com a empresa atual?'].notnull(),'Qual o principal motivo da sua insatisfação com a empresa atual?'].apply(lambda x: 1 if 'Salário' in x else 0)

dados.loc[dados['Qual o principal motivo da sua insatisfação com a empresa atual?'].notnull(),'INSATISFACAO'] = dados.loc[dados['Qual o principal motivo da sua insatisfação com a empresa atual?'].notnull(),'Qual o principal motivo da sua insatisfação com a empresa atual?'].apply(lambda x: 1 if 'Salário' in x else 0)

dados['INSATISFACAO'] .value_counts()

#Atribuindo números ao nível de ensino (0 =  Não tenho graduação), 1 = graduação, 2 bacharelado...etc).

dados['NIVEL DE ENSINO'].value_counts()

dados['NIVEL DE ENSINO'] = dados['NIVEL DE ENSINO'].apply(lambda x: 0 if x == 'Não tenho graduação formal' else
                                               1 if x == 'Estudante de Graduação' else
                                               2 if x == 'Graduação/Bacharelado' else
                                               3 if x == 'Pós-graduação' else
                                               4 if x == 'Mestrado' else
                                               5 if x == 'Doutorado ou Phd' else -1)
# %% regressão linear

#selecionando as colunas que vão alimentar o modelo

dados.columns

dados = dados[['IDADE', 'GENERO', 'NAO_BRANCA', 'TEMPO_EXPERIENCIA', 'SETOR', 'REGIAO ONDE MORA', 'NIVEL DE ENSINO','NUMERO DE FUNCIONARIOS', 'SALARIO', 'NOVO_NIVEL']]

#Converte os textos em números

dados = pd.get_dummies(dados, columns=['GENERO', 'SETOR', 'NOVO_NIVEL', 'REGIAO ONDE MORA'], drop_first=True)

X = dados.drop('SALARIO', axis=1)
y = dados['SALARIO']

#divide os dados entre treino e teste

x_train, x_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)

#padroniza os dados

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)
# %% Módulo 7 - Parte 3
# Criando o modelo
model = LinearRegression()

#Treinando o modelo
model.fit(x_train_scaled, y_train)

#Prevendo os valores de salário
y_pred = model.predict(x_test_scaled)
# %% Avaliação do modelo

# Erro quadrático médio - MSE (Média de diferença entre o valor predito e o valor real elevado ao quadrado)

mse = mean_squared_error(y_test, y_pred)

#MAE -  Erro médio da diferença absoluta
mae = mean_absolute_error(y_test, y_pred)

#R² - Quão próximo os dados estão da linha de regressão (Porcentagem da variação da variável resposta)
r2 = r2_score(y_test, y_pred)
# %% comparando os salários com os valores preditos

plt.figure(figsize=(10,6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Valor Real")
plt.ylabel("Valor Predito")
plt.title("Dispersão dos Dados")
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2)
plt.show()

# %%Verificando quais atributos tiveram maior peso

nomes_atributos = x_train.columns

#criando um dataframe com os coeficientes do modelo
coefs = pd.DataFrame(model.coef_, columns=['coeficientes'], index= nomes_atributos)

#ordenando os valores pra ver qual está influenciando mais
coefs = coefs.sort_values(by='coeficientes', ascending=False)

#plotando um grpafico de barras
coefs.plot.barh(figsize=(8,6))
plt.axvline(x=0, color="red")
          
