def porcentagem(l, p):
	return ((l*100.0)/p)

letra    = raw_input()
palavras = raw_input().split(" ")
qtd      = 0

for i in range(len(palavras)):
	palavra=palavras[i]
	for j in palavra:
		if j == letra:
			qtd += 1
			break

resultado=porcentagem(qtd, len(palavras))
print "%0.1f" %resultado