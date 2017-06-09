# coding: utf8

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1215

abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z',]
except_count = 0
lista = []

while True:
	try:
		palavras = raw_input().split()
		lista += palavras
	except:
		break
		

s = set()

lista_2 = []
for p in lista:
	p = p.lower()
	lista_2 += p.split('-')

lista_3 = []
for p in lista_2:
	lista_3 += p.split("'")


for p in lista_3:
	for i, c in enumerate(p):

		if c not in abc:
			p = p[:i]
			break

	s.add(p)


lista_3 = list(s)
lista_3.sort()

for l in lista_3[:]:
	print l
