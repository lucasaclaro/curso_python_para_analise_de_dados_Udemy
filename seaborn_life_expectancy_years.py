import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly as px

# Tabela de expectativa de vida nos países
#px.data.gapminder()
df = px.data.gapminder().query("country=='Brazil'").set_index('year') #Seleciona a coluna Brazil e coloca como índice o ano
print(df)

#Gráfico sobre a expectativo de vida ao longo dos anos no Brasil
#plt.plot(df.index, df['gdpPercap']) # O eixo X recebe os valores do index (anos) e o eixo Y recebe os valores do PIB per capita
#plt.title('PIB per capita do Brasil')
#plt.ylabel('PIB per capita')
#plt.xlabel('Tempo')
#plt.show()


#Gráfico sobre a relação entre a expectativa de vida e o PIB no Brasil
#plt.plot(df['lifeExp'], df['gdpPercap'])
#plt.title('Relação entre expectativa de vida e PIB no Brasil')
#plt.ylabel('PIB per capita')
#plt.xlabel('Expectativa de vida')
#plt.show()

#Gráfico sobre a relação entre a expectativa de vida e o PIB no Brasil
#plt.figure(figsize=(12, 4))
#plt.scatter(df['lifeExp'], df['gdpPercap'], cmap='viridis')
#plt.title('Relação entre expectativa de vida e PIB no Brasil')
#plt.ylabel('PIB per capita')
#plt.xlabel('Expectativa de vida')
#plt.show()

#Gráfico sobre o crescimento da população brasileira
#plt.bar(x=df.index, height=df['pop'], color='red')
#plt.title('Crescimento da populção brasileira')
#plt.show()

