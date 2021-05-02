def boredom(n, seq):
  maximo = pow(10,5) + 1  
  array = [0]*maximo
  for m in seq:
    array[m]+=1
  pontos = [[0]*2 for m in range(maximo)]
  pontos[1] = [array[1],0]
  
  for m in range(2,maximo):
    for i in range(2):
      if i == 1:
        pontos[m][i] = array[m] * m + max(pontos[m-2][0], pontos[m-2][1])
      else: 
        pontos[m][i] = max(pontos[m-1][0], pontos[m-1][1])
  
  print(max(pontos[maximo-1][0], pontos[maximo-1][1]))

n = int(input())
seq = list(map(int, input().split()))
boredom(n, seq)