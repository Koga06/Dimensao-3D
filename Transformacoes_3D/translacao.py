import numpy as np

#translada=[tx, ty, tz]

def translacao3D(vertices, translada):
    tx, ty, tz = translada

    matriz_translacao = np.array([
        [ 1,  0,  0, 0],
        [ 0,  1,  0, 0],
        [ 0,  0,  1, 0],
        [tx, ty, tz, 1]
    ])

    vertices_transladados = vertices @ matriz_translacao

    return vertices_transladados