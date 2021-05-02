

## Q1

n = int(input())
message = input()
semaforo = False

tmn = len(message)-(n-1)

for t in range(tmn):
  
  for i in range(t, t + n):

    if(message[i] == " "):
      semaforo = True
    
    else:
      semaforo = False
      break
  
  if(semaforo):
    print(t)
    break
if(semaforo == False):
  print("vazio")


## Q2

def add_to_list(numbers):
    for i in numbers:
        list_numbers.append(int(i))

numbers = input()
n = int(input())
list_numbers = []
add_to_list(numbers)

x = 0

for number in range(n):

  if( 2 * x + x  < len(list_numbers) -1):
    
    if(list_numbers[x] < list_numbers[x+1]):
    
      list_numbers.remove(list_numbers[x])
      x = x -(number) 
      
    elif(list_numbers[x] > list_numbers[ x + 1]): 
    
      if(min(list_numbers[x:]) != list_numbers[x + 1]):
        list_numbers.remove(min(list_numbers[x:]))
     
      else: 
        list_numbers.remove(list_numbers[x + 1])
        x = x - (number +1)

    else:
      list_numbers.remove(min(list_numbers))
  print(x)


return_numbers = ''

for num in list_numbers:
  return_numbers += str(num)

print(return_numbers)




## q3 alternativa
numbers = list(map(int, input().split()))
first = -1


for number in range(len(numbers)):

    front, back = False, False
    
    for n in range(len(numbers)):
        if (number != n) and ((numbers[n] == numbers[number] // 3 and numbers[numbe00r] % 3 == 0) or numbers[n] == numbers[number] * 2):
            front = True
            break
   
    for n in range(len(numbers)):
        if (number != n) and (numbers[n] == numbers[number] * 3 or (numbers[n] == numbers[number] // 2 and numbers[number] % 2 == 0)):
            back = True
            break

    if front and not back:
        first = number
  
    if first != -1:
        break

sequence[0] = sequence[0] * len(numbers)
sequence[0] = numbers[first]

for number in range(1, len(sequence)):
    num = sequence[number - 1]
    print(num)
    if num // 3 in numbers:
        sequence[number] = num // 3
    elif num * 2 in numbers:
        sequence[number] = num * 2
        
print(sequence)


##q4

numbers = list(map(int, input().split()))

n = len(numbers)
 
def select_numbers(x, y, list_numbers):
    if len(x) == list_numbers:
        for y in x:
            print(y, end=' ')

    for y in list_numbers:
        if x[y] * 2 == y or x[y] / 3 == float(y):
            new_numbers = copy(list_numbers)
            new_numbers.remove(y)
            select_numbers(x + [y], y + 1, new_numbers)
 
 
for i in numbers:
    list_numbers = copy(numbers)
    list_numbers.remove(i)
    select_numbers([i], 0, n)



## Q5

def coded(num):
  if number == 0 or number==1:
    return number
  
  x = number // 2
  y = number % 2
  z = number // 2

  if x > 1:
    x = coded(x)
  
  if z > 1:
    z = coded(z)
  
  return str(x) + str(y) + str(z)

code = int(input())
print(coded(code))
