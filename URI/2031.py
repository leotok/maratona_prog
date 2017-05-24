def combate(p1, p2):

	if p1 == p2:
		if p1 == "ataque":
			return "Aniquilacao mutua"
		elif p1 == "pedra":
			return "Sem ganhador"
		else:
			return "Ambos venceram"
	elif (p1 == "pedra" and p2 == "papel") or p1 == "ataque":
		return "Jogador 1 venceu"
	else:
		return "Jogador 2 venceu"

n = int(raw_input())

for i in range(n):
	
	p1 = raw_input()
	p2 = raw_input()

	print combate(p1, p2)
