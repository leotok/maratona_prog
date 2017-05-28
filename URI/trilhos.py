# https://www.urionlinejudge.com.br/judge/pt/problems/view/1062

from collections import deque

def debug():
	print top_a 
	print pilha_estacao
	print pilha_saida
	print ""

start = True

while True:
	
	num_blocos = int(raw_input())

	if num_blocos == 0:
		break

	elif not start:
		print ""
	else:
		start = False

	while True:
		saida = raw_input()
		if saida == "0":
			break

		saida = map(int, saida.split())[::-1]

		pilha_estacao = deque()
		pilha_saida = deque(saida)
		top_a = 1

		resp = True

		for i in xrange(num_blocos):

			if pilha_saida and pilha_estacao and pilha_saida[-1] == pilha_estacao[-1]:
					pilha_saida.pop()
					pilha_estacao.pop()

			elif pilha_saida and pilha_saida[-1] == top_a:
				pilha_saida.pop()		

			elif pilha_saida and pilha_saida[-1] > top_a:
				while pilha_saida and pilha_saida[-1] != top_a:
					pilha_estacao.append(top_a)
					top_a += 1

				top_a += 1
				pilha_saida.pop()	

			else:
				resp = False
				break					

		print "Yes" if resp else "No"

