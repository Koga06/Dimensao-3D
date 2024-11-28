import numpy as np
# Aplique a correta rotação nos eixos X e Z.

# x'= zsin + xcos
# y'= y
# z'= zcos - xsin

#    x'  y'  z'
#x   1   0   0   0   
#y   0   1   0   0
#z   0   0   1   0
#    0   0   0   1

def rotacaoXZ3D(vertices, angulo):
    # calcula o centro geometrico
    x = vertices[:, 0].mean()
    y = vertices[:, 1].mean()
    z = vertices[:, 2].mean()

    angulo = np.radians(angulo)

    # cria matriz de translacao inversa, para levar a origem
    transOrigem = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [-x, -y, -z, 1]
    ])
    
    # cria matriz de rotacao
    #xcos   0   -xsin
    #  0    1     0
    #zsin   0    zcos
    rotacaoXZ = np.array([
        [np.cos(angulo), 0, -np.sin(angulo), 0],
        [np.sin(angulo), 1, np.cos(angulo), 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    # cria a matriz de translacao normal para voltar ao ponto original
    transOriginal = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, z, 1]
    ])

    vertices_rotacionados = vertices @ transOrigem @ rotacaoXZ @ transOriginal
    return vertices_rotacionados