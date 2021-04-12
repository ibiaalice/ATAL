a, b = map(int, input().split())

lista = [b]


while (b != a):
	if (b % 10 == 1):
		b //= 10
	elif (b % 2 == 0 and b > 0):
		b //= 2
	else:
		break

	lista.append(b)

if (a == b):
	
	lista.reverse()
	print('YES')
	print(len(lista))

	for i in lista:
		print(i, end = ' ')
else:
	print('NO')