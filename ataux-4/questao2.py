n, m = map(int,input().split())
t = m
grafo = [[] for i in range( n + 1 )]
 
while t > 0:
    ai,bi = map(int,input().split())
    grafo[ai].append(bi)
    grafo[bi].append(ai)
    t -= 1

minimo = n * 3
 
for i in range(1 , n-1):
    if len(grafo[i]) < 2:
        continue

    else:
        for j in grafo[i]:
            if len(grafo[j]) < 2:
                continue

            else:
                for k in grafo[j]:
                    if k in grafo[i]:

                        aux = len(grafo[i]) + len(grafo[j]) + len(grafo[k]) - 6
                        if aux < minimo:
                            minimo = aux
if minimo < n*3:
    print(minimo)
else:
    print(-1)