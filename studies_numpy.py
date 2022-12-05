import numpy as np

#Criar uma matriz de uma dimensão
matriz_1d = np.array([10, 20, 30, 40, 50])
matriz_2d = np.array([
                        [10, 9, 8, 7, 6],
                        [5, 4, 3, 2,1 ]
                    ])
matriz_3d = np.array([
                       [15, 14, 13, 12, 11],
                       [10, 9, 8, 7, 6],
                       [5, 4, 3, 2, 1]
                    ])
#Verificar dimensões
print(matriz_3d.shape) #retorna (3, 5), indicando 3 dimensões com 5 valores em cada

#Percorrer matriz
for dados in matriz_3d:
    print(dados)