import numpy as np
from codificaVertice import encodeVert

#Objeto Triangulo
arestas = np.array([(0,1),(1,2),(2,0)])
vertices = np.array([[1,1,1],[3,1,1],[2,3,1]])

#Area de recorte
verticesCLIP = np.array([[2,1,1] ,[5,1,1],[5,4,1],[2,4,1]])
arestasCLIP = np.array([(0,1),(1,2),(2,3),(3,0)])

listCodes = []

# ANÁLISE DOS VÉRTICES
for p in vertices:
  code = encodeVert(p[:-1],verticesCLIP[:,:-1])
  listCodes.append(code)
  print(p[:-1],code,bin(code))
listCodes = np.array(listCodes)

# ANÁLISE DAS ARESTAS
for ar in arestas:
  pairCodes = listCodes[ar]
  print(pairCodes, vertices[ar[0]], vertices[ar[1]])
  #verificando os pares
  if(pairCodes[0] | pairCodes[1] == 0):
    print('dentro')
  elif(pairCodes[0] & pairCodes[1] != 0):
    print('fora')
  else:
    print('parcialmente')