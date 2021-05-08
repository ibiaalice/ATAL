n, m = map(int, input().strip().split(' '))
if n > m:
    print(n - m)
else:
    margem = {}
    local = [-1] * 2 * m
    escolha = []

    for i in range(1, 2 * m + 1):
        aux = []
        if i > 1:
            aux.append(i - 1)
        if i <= m:
            aux.append(2 * i)
        margem[i] = aux
    local[n] = 0

    escolha.append(n)
    while local[m] == -1:
        cur = escolha.pop(0)
        for j in margem[cur]:
            if local[j] == -1:
                local[j] = local[cur] + 1
                escolha.append(j)
                
    print(local[m])