def dfs(vertice, soma, capital, am):
    soma += len(array[vertice])
    am += 1

    if vertice in capitais:
        capital = True

    usado[vertice] = True
    for i in array[vertice]:
        if not usado[i]:
            tmp, am, soma = dfs(i, soma, capital, am)
            capital |= tmp
    return [capital, am, soma]
 
n, m, k = [int(i) for i in input().split()]

array = []
for i in range(n):
    array.append([]) 
capitais = [int(i) - 1 for i in input().split()]

for i in range(m):
    u, v = [int(i) - 1 for i in input().split()]
    array[u].append(v)
    array[v].append(u)
 
result = 0
usado = [False] * n
auxiliar = []

while False in usado:
    auxiliar.append(dfs(usado.index(False), 0, False, 0))
    auxiliar[len(auxiliar) - 1][2] /= 2
 
for i in range(len(auxiliar)):
    result -= auxiliar[i][2]
 
auxiliar.sort(reverse=True)

total_ns = auxiliar[0][1]

for i in range(1, len(auxiliar)):
    if not auxiliar[i][0]:
        total_ns += auxiliar[i][1]
        
    else:
        result += auxiliar[i][1] * (auxiliar[i][1] - 1) / 2

result += (total_ns) * (total_ns - 1) / 2
print(int(result))