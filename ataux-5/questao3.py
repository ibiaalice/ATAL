n, m = map(int, input().split())
cidades_possiveis = [list(map(int, input().split())) for _ in range(m)]
pares = [[True for j in range(n+1)] for i in range(n+1)]
 
for par in cidades_possiveis:
    pares[par[0]][par[1]] = False
    pares[par[1]][par[0]] = False
 
par_possivel = -1
 
for i in range(1, n+1):
    aux = True
    for j in range(1, n+1):
        aux &= pares[i][j]
        if not aux:
            break
    if aux:
        par_possivel = i
        break
 
print(n-1)
 
for i in range(1, n + 1):
    if i != par_possivel:
        print(par_possivel, i)