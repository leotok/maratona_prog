# https://www.urionlinejudge.com.br/judge/pt/problems/view/1256

from collections import defaultdict

n = int(raw_input())

start = True

for _ in xrange(n):

	if start:
		start = False
	else:
		print
		
	m, c = map(int, raw_input().split())
	chaves = map(int, raw_input().split())

	tabela = defaultdict(list)

	for chave in chaves:
		pos = chave % m
		tabela[pos].append(chave)

	for i in xrange(m):
		print "%d ->" % i,

		for l in tabela[i]:
			print "%d ->" % l,

		print "\\"
