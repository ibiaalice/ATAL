#### Kill 'Em All


loop = int(input())
ataque = []
pontos = []

for i in range(0, loop):
	ataque.append(int(input().split(" ")[1]))
	pontos.append(input().split(" "))
 
for i in range(0,loop):

    local_atual = []
    local_escondido = []
    
    for j in range(0, len(pontos[i])):
        local_atual.append(int(pontos[i][j]))
    
    a = set(local_atual)
    local_escondido = list(a)
    local_escondido.sort(reverse=True)
    count = 0
    
    for j in range(0,len(local_escondido)):
        atack_atual = (ataque[i] * j)

        if local_escondido[j] > atack_atual:
            count += 1
        else:
            print(count)
            break
        
        if count == len(local_escondido):
            print(count)
            break
        