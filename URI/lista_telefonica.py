
while True:

	try:
		n = int(raw_input())
	except:
		break

	lista = []

	for i in xrange(n):
		telefone = raw_input()
		lista.append(telefone)

	lista.sort()

	telefone_anterior = ""
	economia_total = 0

	for telefone in lista:
		economia = 0

		for i in xrange(len(telefone_anterior)):
			if telefone[i] != telefone_anterior[i]:
				break
			else:
				economia += 1

		economia_total += economia
		telefone_anterior = telefone
	print economia_total