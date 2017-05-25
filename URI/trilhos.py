from collections import deque

while True:

	num_blocos = int(raw_input())
	if num_blocos == 0:
		break

	while True:
		trem = list(range(num_blocos, 0, -1))
		# trem = list(range(1, num_blocos + 1))
		saida = raw_input()

		if saida == "0":
			break

		saida = map(int, saida.split())

		pilha_entrada = deque(trem)
		pilha_estacao = deque()
		pilha_saida = deque(saida)

		
		s = pilha_saida[-1]
		e = pilha_entrada[-1]
		p = -1

		resp = True

		while len(pilha_saida) > 0:
			# print s, e, p
			# print pilha_entrada
			# print pilha_estacao
			# print pilha_saida

			# print ""

			if s == e:
				pilha_saida.pop()
				if len(pilha_saida) > 0:
					s = pilha_saida[-1]
				else:
					s = -1

				pilha_entrada.pop()
				if len(pilha_entrada) > 0:
					e = pilha_entrada[-1]
				else:
					e = -1
			else:
				achou = False
				for b in pilha_estacao:
					if s == b:
						achou = True
						# print "achou"

				if achou:
					pilha_saida.pop()
					if len(pilha_saida) > 0:
						s = pilha_saida[-1]
					else:
						s = -1

					pilha_estacao.pop()
					if len(pilha_estacao) > 0:
						p = pilha_estacao[-1]
					else:
						p = -1

				else:
					if len(pilha_entrada) == 0:
						resp = False
						break
					else:
						pilha_estacao.append(pilha_entrada.pop())
						p = pilha_estacao[-1]

				if len(pilha_entrada) > 0:
					e = pilha_entrada[-1]
				else:
					e = -1

		print "Yes" if resp else "No"
	print