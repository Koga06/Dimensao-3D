import numpy as np
# Aplique a correta rotação nos eixos Y e Z.

# x' = x
# y'= ycos - zsin
# z'= ysin + zcos

#    x'  y'  z'
#x   1   0   0   0   
#y   0   1   0   0
#z   0   0   1   0
#    0   0   0   1

def rotacaoYZ3D(vertices, angulo):
    # calcula o centro geometrico
    x = vertices[:, 0].mean()
    y = vertices[:, 1].mean()
    z = vertices[:, 2].mean()

    angulo = np.radians(angulo)

    # cria matriz de translacao inversa, para levar a origem
    transOrigem = np.array([
        [1, np.cos(angulo), -np.sin(angulo), 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [-x, -y, -z, 1]
    ])
    
    # cria matriz de rotacao
    #  1      0       0
    #  0     ycos    ysin
    #  0    -zsin    zcos
    rotacaoYZ = np.array([
        [1, 0, 0, 0],
        [0, np.cos(angulo), np.sin(angulo), 0],
        [0, -np.sin(angulo), np.cos(angulo), 0],
        [0, 0, 0, 1]
    ])

    # cria a matriz de translacao normal para voltar ao ponto original
    transOriginal = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, z, 1]
    ])

    vertices_rotacionados = vertices @ transOrigem @ rotacaoYZ @ transOriginal
    return vertices_rotacionados