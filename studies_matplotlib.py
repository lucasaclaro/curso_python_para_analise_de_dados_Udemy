import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(7)

y = np.random.randint(low=1, high=1500, size=10)



##### Gerar gráfico #####
#plt.plot(y)
#plt.show()



##### Editar gráfico #####
# Inserir a primeira linha no plot
#plt.plot(y, color='#749187', marker='o', ms=5, mec='black', ls='-.')  #marker, ms, mec e ls se referem à linha

# Inserir a segunda linha no plot
#plt.plot(y*2, marker='+', color='k', ms=5) # Valor do eixo Y multiplicados a 2

# Rótulos
#plt.xlabel('Eixo X', color='red', size=12)
#plt.ylabel('Eixo Y')
#plt.title('Título', loc='left')

# Gridlines
#plt.grid(axis='y', color='gray', linestyle='--', linewidth=1, alpha=0.8) # Axis por ser nos eixo X, Y ou both
#plt.show()


##### Gráficos com subplots ######
np.random.seed(6)
x = np.arange(1, 11)
y1 = np.random.randint(1, 400, 10)
y2 = np.random.randint(150, 500, 10)
y3 = np.random.randint(200, 600, 10)

plt.figure(figsize=(15, 5))
plt.suptitle('Figure', fontsize=15)

plt.subplot(1, 3, 1) #1 linha, 3 gráficos e esse será o gráfico 1
plt.plot(x, y1, color='black')
plt.title('Subplot 1', pad=10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1, 3, 2) #1 linha, 3 gráficos e esse será o gráfico 2
plt.plot(x, y2, color='green')
plt.title('Subplot 2', pad=10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.subplot(1, 3, 3) #1 linha, 3 gráficos e esse será o gráfico 3
plt.plot(x, y3, color='red')
plt.title('Subplot 3', pad=10)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

plt.tight_layout(pad=4) #aumentar o espaçamento entre os subplots
plt.show()