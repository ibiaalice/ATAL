#### Equivalent Strings

def divide_letras(palavra):
    tamanho = len(palavra)

    if (tamanho % 2 == 1):
        return palavra

    tamanho = tamanho // 2    
    esquerda = divide_letras(palavra[:tamanho])
    direita = divide_letras(palavra[tamanho:])
    
    if (esquerda < direita):
        return (esquerda + direita) 
    else:
        return (direita + esquerda)
 

a = input()
b = input()

if(divide_letras(a) == divide_letras(b)):
    print('YES')
else:
    print('NO')
