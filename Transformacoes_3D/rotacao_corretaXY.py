import numpy as np
# Aplique a correta rotação nos eixos X e Y.

# x'= xcos - ysin
# y'= xsin + yscos
# z'= z

#    x'  y'  z'
#x   1   0   0   0   
#y   0   1   0   0
#z   0   0   1   0
#    0   0   0   1

def rotacaoXY3D(vertices, angulo):
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
    #   xcos    xsin    0
    #  -ysin    ycos    0
    #  0         0      1
    rotacaoXY = np.array([
        [np.cos(angulo), np.sin(angulo), 0, 0],
        [-np.sin(angulo), np.cos(angulo), 0, 0],
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

    vertices_rotacionados = vertices @ transOrigem @ rotacaoXY @ transOriginal
    return vertices_rotacionados