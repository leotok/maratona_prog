# https://www.urionlinejudge.com.br/judge/pt/problems/view/1162

num_casos = int(raw_input())

def bs(l):
	c = 0
	for i in xrange(len(l)):
		fim = True
		for j in xrange(i + 1, len(l)):
			if l[i] > l[j]:
				l[i], l[j] = l[j], l[i]
				fim = False
				c += 1
		if fim:
			break
	return c

def n(l):
	i = 0
	qtd_mov = 0

	while i < len(l):
		if i + 1 != l[i]:
			# qtd_mov += 2 * (l[i] - l[l[i] - 1]) - 1
			qtd_mov += 1
			l[l[i] - 1], l[i] = l[i], l[l[i] - 1]
		else:
			i += 1
	return qtd_mov

while num_casos:

	tam = int(raw_input())
	read = map(int, raw_input().split())

	i = 0
	qtd_mov = 0
	
	print 'Optimal train swapping takes %d swaps.' % n(read)
	num_casos -= 1
