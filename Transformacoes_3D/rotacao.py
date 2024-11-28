import numpy as np

def rotacao3D(vertices, angulo):
    angulo = np.radians(angulo)
    
    matriz_rotacao = np.array([
        [np.cos(angulo), 0, -np.sin(angulo), 0],
        [0,              1,  0,              0],
        [np.sin(angulo), 0,  np.cos(angulo), 0],
        [0,              0,  0,              1]
    ])

    vertices_rotacionados = vertices @ matriz_rotacao

    return vertices_rotacionados