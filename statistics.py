import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data_base = sns.load_dataset('iris') #carregar base de dados do próprio seaborn
#print(data_base)

#print(data_base.shape) #quantidade de linhas e colunas

#Média
media = data_base['petal_length'].mean()
#print(media)

#Moda - valor que mais aparece entre os observados
moda = data_base['petal_length'].mode()
#print(moda)

#Mediana - é a posição central dos dados
mediana = data_base['petal_length'].median()
#print(mediana)

### Quartis ###
data_base_sepal = data_base['sepal_length'].describe()
#print(data_base_sepal)
#min        4.300000 - valor mínimo
#25%        5.100000 - o primeiro quartil indica que 25% dos dados estão entre 4.3 e 5.1
#50%        5.800000 - o segundo quartil indica que 50% dos dados estão entre 4.3 e 5.8
#75%        6.400000 - o terceiro quartil indica que 75% dos dados estão entre 4.3 e 6.4
#max        7.900000 - valor máximo
#graphic_q = sns.boxplot(data_base['sepal_length'])
#plt.show()

### Dispersão ###
data_base_sepal_max = data_base['sepal_length'].max()
data_base_sepal_min = data_base['sepal_length'].min()
#print(data_base_sepal_max)
#print(data_base_sepal_min)
amplitude_total = data_base_sepal_max - data_base_sepal_min #é a diferença entre o valor máximo e mínimo
amplitude_interquartilica = data_base['sepal_length'].describe()[6:7].values - data_base['sepal_length'].describe()[4:5].values #é a diferença entre o terceiro e o primeiro quartil
#print(amplitude_interquartilica)
amplitude_semiinterquartifica = amplitude_interquartilica / 2 #é a diferença interquartilica dividido por 2
#print(amplitude_semiinterquartifica)
variancia = data_base['sepal_length'].var() #é o quão distante os valores está da média
#print(variancia)
desvio_padrao = data_base['sepal_length'].std() #é a raiz quadrada da variância. Quanto mais próximo de 0 os valores, mais homogêneos são os dados
#print(desvio_padrao)


#Simetria de dados: simétrica se média == moda ou As == 0 / assimétrica negativa se média <= mediana <= moda ou As < 0 / assimétrica positiva se moda <= mediana <= média ou As > 0
assimetria = data_base['sepal_length'].skew()
#print(assimetria) #nesse caso o resultado foi 0.31, indicando assimetria positiva
assimetria_graphic = sns.kdeplot(data_base['sepal_length'])
#plt.show()

#Medidas de curtose:
#Leptocúrtica: curva com frequência fechada, indicando que os dados estão fortemente concentrados em torno do centro. K < 0.263
#Mesocúrtica: quando os dados estão razoavelmente concentrados em torno do centro. K = 0.263
#Platicúrtica: curva com frequência aberta, indiciando que os dados estão fracamente concentrados em torno do centro. K > 0.263
curtose = data_base['sepal_length'].kurtosis()
#print(curtose) #nesse caso o resultado foi -0.55, indicando que os dados estão fortemente concentrados no centro (leptocúrtica)
#assimetria_graphic = sns.kdeplot(data_base['sepal_length'])
#plt.show()

#Correlação de Pearson: um intervalo entre 1 e -1, onde 0 indica que não há correlação entre duas variáveis
#Por exemplo, na premissa aumentando os descontos, aumentam as vendas, se a medida for 0, isso indicia que não correlação entre as duas variáveis
#Valor maior que 0 indica uma associação positiva, quando um aumenta, o outro também aumenta
#Valor menor que 0 inidica uma associação negativa, quando um aumenta, o outro diminui
correlacao_pearson = data_base.corr()
#print(correlacao)
correlaca_pearson_graphic = sns.heatmap(correlacao_pearson, annot=True)
#plt.show()

#Correlação de Spearman: é possível utilizar quando existem relações não lineares
correlacao_spearman = data_base.corr('spearman')
#print(correlacao_spearman)
correlacao_spearman_graphic = sns.heatmap(correlacao_spearman, annot=True)
#plt.show()



