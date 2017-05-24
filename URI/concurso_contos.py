import math

while True:
	try:
		read = raw_input().split(" ")
	except EOFError:
		break
	
	num_palavras = float(read[0])
	num_linhas = float(read[1])
	num_carac = float(read[2])

	poema = raw_input()

	print int(math.ceil((len(poema) / num_carac) / num_linhas))
