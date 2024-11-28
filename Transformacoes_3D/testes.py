import generate_view as gv
from escala import escala3D
from rotacao import rotacao3D

# 01

vertices, arestas = gv.criaPiramide()
novos_vertices = escala3D(vertices, [1, 0.5, 0.5])#sx=1, sy=0.5, sz=0.5
gv.desenhaFigura(vertices, arestas, novos_vertices) #Novos Vértices estão em vermelho

# 02

vertices, arestas = gv.criaPiramide()
novos_vertices = rotacao3D(vertices, 20) #angulo=20
gv.desenhaFigura(vertices, arestas, novos_vertices) #Novos Vértices estão em vermelho

# 03
# 04
# 05.a
# 05.b
# 05.c