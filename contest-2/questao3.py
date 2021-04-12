n, m = map(int, input().split())

grafico = []

for i in range(n):
  grafico.append(input())
 
 
def vizinho(vertice, cor):
  x, y = vertice
  lista = []
  if (x > 0) and (grafico[x - 1][y] == cor):
    lista.append((x - 1, y))
  
  if (y > 0) and (grafico[x][y - 1] == cor):
    lista.append((x, y - 1))

  if (x < n - 1) and (grafico[x + 1][y] == cor):
    lista.append((x + 1, y))

  if (y < m - 1) and (grafico[x][y + 1] == cor):
    lista.append((x, y + 1))

  return lista
 
 
def encontra_circulos(x, y):
  cor = grafico[x][y]
  visitado = set()
  pilha = [((x, y), None)]

  while pilha:
    v, no = pilha.pop()
    
    if v in visitado:
      return set()
    
    visitado.add(v)
    
    for u in vizinho(v, cor):
     
      if u != no:
        pilha.append((u, v))
  
  return visitado
 
 
visitado = set()

for i in range(n):
  for j in range(m):

    if (i, j) not in visitado:
      t = encontra_circulos(i, j)

      if not t:

        print('Yes')
        exit()

      visitado |= t
 
print('No')