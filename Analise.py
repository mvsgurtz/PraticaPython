
import pandas as pd

# importar tabela
tabela = pd.read_csv("telecom_users.csv")
print(tabela)

# Analisar a base de dados
tabela = tabela.drop("Unnamed: 0", axis=1)  
f"""Prezados, bom dia

O faturamento de ontem foi de: R$2,917,311.00
A quantidade de produtos foi de: 15,227

Abs ! 
Marcos Vincius Goulart"""

print(tabela)

# entender e descobrir as "cagadas" na base de dados!

# reconhecer valores que estão de forma errada

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors= "coerce" )

# - Valores vazios
# deletando as colunas vazias
# axis = 0 _> linha ou axis = 1 _> coluna
tabela =  tabela.dropna(how="all", axis=1)
# deletando as colunas vazias
tabela = tabela.dropna(how="any", axis=0)

print(tabela.info())

# Análise Inicial
# Como estão os nossos cancelamentos?
print(tabela["Churn"].value_counts())
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

# Analise detalhada

import plotly.express as px

for coluna in tabela.columns:
    grafico = px.histogram(tabela, x = coluna, color= "Churn")
    grafico.show()