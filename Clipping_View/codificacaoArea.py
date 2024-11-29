#Codificação das áreas
codeTOP=1<<3    #1000
codeBTM=1<<2    #0100
codeLEFT=1      #0001
codeRIGHT=1<<1  #0010

print('TOP',codeTOP,bin(codeTOP))
print('BTM',codeBTM,bin(codeBTM))
print('LEFT',codeLEFT,bin(codeLEFT))
print('RIGHT',codeRIGHT,bin(codeRIGHT))

# Teste 1000 (8) | 0100 (4) = 1100 (12)
# Essa expressão tá combinando os valores
x= codeTOP | codeRIGHT
print(x,bin(x))