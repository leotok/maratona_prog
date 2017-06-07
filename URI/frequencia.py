from collections import defaultdict

start = True

while True:

	try:
		entrada = raw_input()
	except:
		break

	if start:
		start = False
	else:
		print ""

	freq = defaultdict(int)

	for c in entrada:
		freq[c] += 1

	lista = []
	for key, value in freq.items():
		lista.append((ord(key), value))

	lista.sort(key=lambda x: (x[1], -x[0]))

	for l in lista:
		print l[0], l[1]