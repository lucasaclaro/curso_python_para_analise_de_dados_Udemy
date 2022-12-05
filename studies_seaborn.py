import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Definir o tema dos gráficos
sns.set_theme(style='darkgrid')

data_base = sns.load_dataset('tips') # base de dados do próprio seaborn sobre gorjetas em restaurantes

#Renomear colunas
data_base.rename(columns={
    'total_bill': "Total da conta",
    'tip': 'Gorjeta',
    'sex': 'Sexo',
    'smoker': 'Fumante',
    'day': 'Dia',
    'time': 'Refeição',
    'size': 'Pessoas na mesa'
}, inplace=True) # inplace é para aplicar a transformação na base de dados

#print(data_base)

#Gráfico relplot
#sns.relplot(x='Total da conta', y='Gorjeta', data=data_base)
#plt.show()

#Gráfico de linha com dois eixos
#sns.relplot(x='Total da conta', y='Gorjeta', data=data_base, kind='line')
#plt.show()

#Gráfico hisplot
#sns.histplot(data=data_base, x='Total da conta', hue='Fumante')
#plt.show()

#Grafico barplot
#sns.barplot(data=data_base, x='Sexo', y='Total da conta', hue='Fumante')
#plt.show()

#Pairplot
#sns.pairplot(data_base)
#plt.show()
#sns.pairplot(data_base, hue='Sexo')
#plt.show()
