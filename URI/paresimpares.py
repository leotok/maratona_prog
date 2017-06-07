# https://www.urionlinejudge.com.br/judge/pt/problems/view/1259

n = int(raw_input())

pares = []
impares = []
for i in xrange(n):

	num = int(raw_input())
	if num % 2 ==  0:
		pares.append(num)
	else:
		impares.append(num)
	
pares.sort()
impares.sort(reverse=True)

lista = pares + impares

for num in lista:
	print num