# https://www.urionlinejudge.com.br/judge/pt/problems/view/1084
import heapq
from collections import deque

while True:

	n, d = map(int, raw_input().split())
	pilha = deque()

	if not n and not d:
		break

	entrada = raw_input()

  	for i in xrange(n):
  		valor = ord(entrada[i]) - ord('0')
		while len(pilha) > 0 and pilha[-1] < valor and d > 0:
			pilha.pop()
			d -= 1
		pilha.append(valor)

	while d:
		pilha.pop()
		d -= 1

	saida = ""
	for num in pilha:
		saida += str(num)

	print saida
	