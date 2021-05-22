def bfs():
    while len(fila) > 0:
        atual = fila.pop(0)

        if atual < n and e[atual + 1] > e[atual] + 1:
            e[atual+1]=e[atual]+1

            fila.append(atual + 1)

        if atual > 1 and e[atual - 1] > e[atual]+1:
            e[atual - 1] = e[atual] + 1
            fila.append(atual - 1)
        
        if e[ cruzamentos[atual] ] > e[atual] + 1:
            e[cruzamentos[atual]] = e[atual]+1
            
            fila.append(cruzamentos[atual])
 
n = int(input())
entrada = input().split()
cruzamentos = [0] + [int(x) for x in entrada]
e = [float('inf') for x in range( n + 1 )]
e[1] = 0
fila=[1]
bfs()
 
print(' '.join(str(i) for i in e[1:]))