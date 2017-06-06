# https://www.urionlinejudge.com.br/judge/pt/problems/view/1082

from collections import defaultdict

casos_teste = int(raw_input())
abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','z']

for n in xrange(1, casos_teste + 1):
	print "Case #%d:" %n
	v, e = map(int, raw_input().split())

	graph = defaultdict(set)
	for i in xrange(e):
		x, y = raw_input().split()
		
		graph[x].add(y)
		graph[y].add(x)

	num_conexo = 0
	visitados = defaultdict(int)
	
	for c in abc[:v]:
		nodes = []
		if not visitados[c]:
			nodes.append(c)
			visitados[c] = 1
			prox = [c]
			num_conexo += 1
			while len(prox) != 0:
				level = []
				for node in prox:
					for vizinho in graph[node]:
						if not visitados[vizinho]:
							prox.append(vizinho)
							level.append(vizinho)
							nodes.append(vizinho)
							visitados[vizinho] = 1
				prox = level
		if nodes:
			format_str = ""
			nodes.sort()
			for node in nodes:
				format_str += node + ","
			print format_str

	print "%d connected components" % num_conexo
	if n != casos_teste + 2:
		print ""
		
	casos_teste -= 1