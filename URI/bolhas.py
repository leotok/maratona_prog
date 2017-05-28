while True:
	read = map(int, raw_input().split())
	n = read[0]
	if n == 0:
		break
	read = read[1:]
	
	i = 0
	qtd_mov = 0

	while i < len(read):
		if i + 1 != read[i]:
			qtd_mov += 2 * (read[read[i] - 1] - read[i]) - 1
			read[read[i] - 1], read[i] = read[i], read[read[i] - 1]
		else:
			i += 1

	print "Marcelo" if qtd_mov % 2 == 1 else "Carlos"


