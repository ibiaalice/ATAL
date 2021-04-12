n, xi, yi, valor = int(input()), [], [], 0

for i in range(n):
    x, y = map(int, input().split())

    xi.append({x})
    yi.append({y})


for i in range(n - 1):
    for j in range(i + 1, n):

        if xi[i] & xi[j] or yi[i] & yi[j]:

            xi[j] |= xi[i]
            yi[j] |= yi[i]
            
            valor += 1
            
            break

valor_saida = n - valor - 1

print(valor_saida)