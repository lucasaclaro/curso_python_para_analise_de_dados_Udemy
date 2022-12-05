import pandas as pd
import numpy as np


# Abrir dataframe
df = pd.read_csv('data/StudentsPerformance.csv')
#print(df)

# 5 primeiras linhas
#print(df.head())

# 5 últimas linhas
#print(df.tail())

# Qtdo de linhas e colunas
#print(df.shape)

# Colunas
#print(df.columns)

# Verificar linhas duplicadas
#print(df.duplicated().sum())

# Informações genéricas
#print(df.info())

# Verificar a existência de Nan
#print(df.isna().sum())

# Sumário estatístico
#print(df.describe())
# Ao visualizar esse exemplo é possível interpretar da seguinte maneira as porcentagens:
# 25% dos alunos tirou em matemática nota menor que 57 / 50% tirou nota menor que 66 / 75% tirou nota menor quer 77

# Qtd de valores únicos
#print(df.nunique())

# Valores únicos
#print(df['gender'].unique())

# Frequência entre os valores
#print(df.gender.value_counts())
#print(df.lunch.value_counts())

# Ordenar de acordo com os valores de uma coluna
#print(df.sort_values(['math score']).reset_index(drop = True))

# Consultas
print(df[(df.gender == 'male') & (df['test preparation course'] == 'none') & (df['math score'] >= 70 )])
