import numpy as np

#Codificação das áreas
codeTOP=1<<3    #1000
codeBTM=1<<2    #0100
codeLEFT=1      #0001
codeRIGHT=1<<1  #0010

# Essa função codifica a posição de um ponto em relação ao
# retângulo delimitador

# axis=0: Operação ao longo das colunas (processa elementos verticalmente).
# axis=1: Operação ao longo das linhas (processa elementos horizontalmente).

def encodeVert(ponto, retangulo):
    # limites minimos e maximos do retangulo
    xmin, ymin = np.min(retangulo, axis = 0)
    xmax, ymax = np.max(retangulo, axis = 0)

    code = 0

    if(ponto[0] < xmin):
        code = code | codeLEFT
    elif(ponto[0] > xmax):
        code = code | codeRIGHT
    
    if (ponto[1] < ymin):
        code = codeBTM
    elif (ponto[1] > ymax):
        code = codeTOP
    
    return code