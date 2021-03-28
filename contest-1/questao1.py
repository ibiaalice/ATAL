
linha, coluna = map(int,input().split())

matriz =[[*map(int,input().split())] for _ in " "*linha]

variante = int(1e5+2)

l = [1,1] + ([0]*variante)

for x in range(2,variante):
    l[x*x::x]= [1] * ((variante-x*x)//x+1)

for y in range(variante,-1,-1):
    l[y]*= l[y+1] + 1

for z in range(linha):
    for j in range(coluna):
           matriz[z][j]=l[matriz[z][j]]


print(min(min(sum(valor) for valor in matriz),min(sum(valor) for valor in zip(*matriz))))
