import numpy as np

#escala = [sx, sy, sz]

# Cria uma matriz de escala
def mat_escala3D(sx, sy, sz):
    # cria uma matriz identidade 4x4
    m = np.identity(4)

    # altera os valores da diagonal principal, inserindo a escala
    m[0, 0] = sx
    m[1, 1] = sy
    m[2, 2] = sz
    
    return m

# Cria uma matriz de translação
def mat_translacao3D(tx, ty, tz):
    # cria uma matriz de identidade 4x4
    m = np.identity(4)

    # altera a ultima linha pelos translados
    m[3] = np.array([tx, ty, tz, 1])
    
    return m

# Calculo do centro geometrico de um conjunto de vértices
def centro_geometrico(vertices):
    # np.mean calcula a média das cordenadas x, y e z
    mu_x = np.mean(vertices[: ,0])
    mu_y = np.mean(vertices[: ,1])
    mu_z = np.mean(vertices[: ,2])

    # retorna tx, ty e tz
    return [mu_x, mu_y, mu_z]
    
def escala3D_correta(vertices, escala):
    sx, sy, sz = escala
    
    # extrai os fatores de translacao
    tx, ty, tz = centro_geometrico(vertices) 
    
    # cria a matriz de translação inversa
    #para que o centro geométrico fique na origem
    mat_translacao = mat_translacao3D(-tx, -ty, -tz)
    
    # move os vértices para a origem
    novos_vertices = vertices @ mat_translacao

    # cria matriz escala para ajustar tamanho do objeto
    mat_escala = mat_escala3D(sx, sy, sz)
    novos_vertices = novos_vertices @ mat_escala

    # cria a matriz de translacao normal
    # faz com que os vertices voltem a posicao original do centro geometrico
    mat_translacao = mat_translacao3D(tx, ty, tz)
    novos_vertices = novos_vertices @ mat_translacao

    return novos_vertices