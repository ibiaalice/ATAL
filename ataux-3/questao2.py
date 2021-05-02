n = int(input())
matriz = [int(x) for x in input().split()]
consultas = int(input())
b = [[int(x) for x in input().split()] for i in range(0, consultas)]
 
matriz_populada = [[0 for j in range(0, n - i)] for i in range(0, n)]

for i in range(0, n):
    matriz_populada[0][i] = matriz[i]
    
for i in range(1, n):

    for j in range(0, n - i):
        matriz_populada[i][j] = matriz_populada[i - 1][j] ^ matriz_populada[i - 1][j + 1]
        
for i in range(1, n): #

    for j in range(0, n - i):
        matriz_populada[i][j] = max(max(matriz_populada[i][j],matriz_populada[i - 1][j]),matriz_populada[i - 1][j + 1])

for i in range(0, consultas):
    print (matriz_populada[b[i][1] - b[i][0]][b[i][0] - 1]) #