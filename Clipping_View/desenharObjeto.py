import matplotlib.pyplot as plt
import numpy as np

#função para desenhar as arestas e vertices
def drawObjectEdges(vertices,arestas,ax,color='b'):

    ax.scatter(vertices[:, 0], vertices[:, 1], c='r', marker='o')
    for i,p in enumerate(vertices):
        x,y,_ = p
        ax.text(x, y-1, str(i),ha='center')
    for edge in arestas:
        ax.plot(vertices[edge, 0],vertices[edge, 1], c=color)
    ax.set_xlim(-1, 7)
    ax.set_ylim(-1, 7)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')

#Objeto Triangulo
arestas = np.array([(0,1),(1,2),(2,0)])
vertices = np.array([[1,1,1],[3,1,1],[2,3,1]])

#Area de recorte
verticesCLIP = np.array([[2,1,1] ,[5,1,1],[5,4,1],[2,4,1]])
arestasCLIP = np.array([(0,1),(1,2),(2,3),(3,0)])

fig, ax = plt.subplots(figsize=(3, 3))
drawObjectEdges(vertices,arestas,ax,'k') #Cor preta o Triângulo
drawObjectEdges(verticesCLIP,arestasCLIP,ax) #Cor azul o Recorte