#LOSE IT

def filtra_array(n, array):
    
    div4 = 0
    div8 = 0
    div15 = 0        
    div16 = 0
    div23 = 0
    div42 = 0
        
    for i in range(n):
        if(array[i] == 4):
            div4 += 1
            
        elif(array[i] == 8):
            if div4 >0:
                div4 -= 1
                div8 += 1

        elif(array[i] == 15):
            if div8 > 0:
                div8 -= 1
                div15 += 1

        elif(array[i] == 16):
            if div15 > 0:
                div15 -= 1
                div16 += 1

        elif(array[i] == 23):
            if div16 > 0:
                div16 -= 1
                div23 += 1

        elif(array[i] == 42):
            if div23 > 0:
                div23 -= 1
                div42 += 1
            
    return (n-div42 * 6)
 
n = int(input())
array = list(map(int, input().rstrip().split()))

array_bom = filtra_array(n, array)

print(array_bom)