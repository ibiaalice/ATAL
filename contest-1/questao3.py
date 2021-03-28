l,r = map(int , input().split())

saida = -1
 
for m in range(l,r+1):
 s = str(m)
 if len(s) == len(set(s)):
     saida = m
     break
print(saida)