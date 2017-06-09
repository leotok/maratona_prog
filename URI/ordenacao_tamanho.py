# https://www.urionlinejudge.com.br/judge/pt/problems/view/1244

n = int(raw_input())

for i in xrange(n):

	palavras = raw_input().split()

	palavras.sort(key= lambda x: -len(x))

	for p in palavras:
		print p,
	print