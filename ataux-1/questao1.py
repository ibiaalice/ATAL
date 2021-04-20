#### UNIQUE NUMBER

for i in range(int(input())):
    entrada = int(input())
    numeros = [0,1,2,3,4,5,6,7,8,9]
    resposta = ''
	
    while numeros and entrada > 0:
	
    	if entrada >= numeros[-1]:
            resposta += str(numeros[-1])
            entrada -= numeros[-1]
	
    	numeros.pop()
	
    if entrada == 0: 
        print(resposta[::-1])
	
    else:
        print(-1)