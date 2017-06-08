# https://www.urionlinejudge.com.br/judge/pt/problems/view/1215

except_count = 0
lista = []
while True:

	try:
		palavras = raw_input().split()
		raw_input()
		except_count = 0
		lista += palavras
	except:
		except_count += 1

	if except_count == 2:
		break
		
s = set()

for p in lista:
	p = p.lower()

	for i, c in enumerate(p):
		if ord(c) < 97 or ord(c) > 123:
			p = p[:i]
			break
		

	s.add(p)

lista = list(s)
lista.sort()

for l in lista:
	print l

# 96 123