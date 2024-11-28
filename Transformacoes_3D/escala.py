import numpy as np

#Escala = [sx, sy, sx]

def escala3D(vertices, escala):
    fatores_escala = np.array([*escala, 1])

    vertices_escalados = vertices * fatores_escala

    return vertices_escalados