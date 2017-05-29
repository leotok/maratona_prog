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


while num_casos:

	tam = int(raw_input())
	read = map(int, raw_input().split())
	
	print 'Optimal train swapping takes %d swaps.' %bs(read)
	num_casos -= 1
