import numpy as np
import plotly.graph_objects as go

#Defina os valores de vértices e arestas para desenhar uma piramede com 4 vértices.
def criaPiramide():
  vertices_piramede = np.array([
      [3, 3, 3,1],
      [5, 3, 3,1],
      [5, 5, 3,1],
      [3, 5, 3,1],
      [4, 4, 5,1]
      ])
  arestas = [
      (0, 1), (1, 2), (2, 3), (3, 0),  # Face frontal
      (0, 4), (1, 4), (2, 4), (3, 4)   # Arestas de ligação entre as faces
  ]
  return [vertices_piramede, arestas]

def criaCubo():
  # Define as coordenadas dos vértices do cubo
  vertices_cubo = np.array([
      [3, 3, 3,1],
      [5, 3, 3,1],
      [5, 5, 3,1],
      [3, 5, 3,1],
      [3, 3, 5,1],
      [5, 3, 5,1],
      [5, 5, 5,1],
      [3, 5, 5,1]
  ])


  # Define as arestas que conectam os vértices
  arestas = [
      (0, 1), (1, 2), (2, 3), (3, 0),  # Face frontal
      (4, 5), (5, 6), (6, 7), (7, 4),  # Face traseira
      (0, 4), (1, 5), (2, 6), (3, 7)   # Arestas de ligação entre as faces
  ]
  return [vertices_cubo, arestas]

def desenhaFigura(vertices, arestas, novos_vertices=None):
  # Criar um gráfico scatter_3d com os vértices do cubo
  fig = go.Figure(data=[go.Scatter3d(
      x=vertices[:, 0],
      y=vertices[:, 1],
      z=vertices[:, 2],
      mode='markers',
      marker=dict(
          size=5,
          color='blue'
      )
  )])

  #Add new vertexes to draw (novos_vertices)
  if novos_vertices is not None:
    fig.add_trace(go.Scatter3d(
        x=novos_vertices[:, 0],
        y=novos_vertices[:, 1],
        z=novos_vertices[:, 2],
        mode='markers',
        marker=dict(
            size=5,
            color='red'
        )
    ))
    for aresta in arestas:
      fig.add_trace(go.Scatter3d(
          x=[novos_vertices[aresta[0]][0], novos_vertices[aresta[1]][0]],
          y=[novos_vertices[aresta[0]][1], novos_vertices[aresta[1]][1]],
          z=[novos_vertices[aresta[0]][2], novos_vertices[aresta[1]][2]],
          mode='lines',
          line=dict(color='red', width=2)
      ))




  # Adicionar as linhas que representam as arestas
  for aresta in arestas:
    fig.add_trace(go.Scatter3d(
        x=[vertices[aresta[0]][0], vertices[aresta[1]][0]],
        y=[vertices[aresta[0]][1], vertices[aresta[1]][1]],
        z=[vertices[aresta[0]][2], vertices[aresta[1]][2]],
        mode='lines',
        line=dict(color='black', width=2)
    ))



  # Linhas de referência da origem
  fig.add_trace(go.Scatter3d(
      x=[0, 5], y=[0, 0], z=[0, 0], mode='lines', line=dict(color='red', width=2)
  ))
  fig.add_trace(go.Scatter3d(
      x=[0, 0], y=[0, 5], z=[0, 0], mode='lines', line=dict(color='green', width=2)
  ))
  fig.add_trace(go.Scatter3d(
      x=[0, 0], y=[0, 0], z=[0, 5], mode='lines', line=dict(color='blue', width=2)
  ))


  annotations=[]
  for i in range(vertices.shape[0]):
      annotations.append(dict(x=vertices[i, 0], y=vertices[i, 1], z=vertices[i, 2], text=str(i), showarrow=True))

  # Definir os limites dos eixos
  fig.update_layout(scene=dict(
      xaxis=dict(range=[-10, 10]),
      yaxis=dict(range=[-10, 10]),
      zaxis=dict(range=[-10, 10]),
      annotations=annotations
  ))

  fig.update_layout(showlegend=False)

  # Adicionar um título ao gráfico
  fig.update_layout(title='Espaço 3D')
  fig.show()

#########################################################
#####               DESENHANDO FIGURA               #####
#########################################################

vertices, arestas = criaPiramide()
desenhaFigura(vertices, arestas)

#ou para desenhar a figura antiga e a nova (red)
vertices_novos = np.array([
  [2, 3, 2,1],
  [4, 3, 2,1],
  [4, 5, 2,1],
  [2, 5, 2,1],
  [3, 4, 4,1]
  ])
desenhaFigura(vertices, arestas, vertices_novos)