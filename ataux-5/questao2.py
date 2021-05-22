cidade_x, cidade_y = map(int, input().split())
 
cruzamento = [0] * (cidade_x + 1)

for l in range(cidade_x + 1):
    cruzamento[l] = [1] * (cidade_x + 1)
 
for i in range(cidade_y):
    a, b = map(int, input().split())
    cruzamento[a][b] = cruzamento[b][a] = 2
 
x, veiculo, indice = 3 - cruzamento[1][cidade_x], [0] * (cidade_x + 1), 1
d = [cidade_x + 1] * (cidade_x + 1)
tempo_ultimo =  d[1] = 0
 
while indice != cidade_x:
    veiculo[indice] = 1
    for j in range(1, cidade_x + 1):
        if veiculo[j] == 0 and cruzamento[indice][j] == x and d[j] > d[indice] + 1:
            d[j] = d[indice] + 1
    menor = cidade_x + 1
 
    for j in range(1, cidade_x + 1):
        if veiculo[j] == 0 and d[j] < menor:
            menor = d[j]
            indice = j
 
    if menor == cidade_x + 1:
        tempo_ultimo = -1
        break
 
    elif indice == cidade_x:
        tempo_ultimo = d[cidade_x]
        break
 
print(tempo_ultimo)