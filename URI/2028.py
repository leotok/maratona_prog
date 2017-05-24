def fat(n):
	l = [0]
	for i in range(n+1):
		for j in range(i):
			l.append(i)
	return l

tot = 1
while True:
	
	try:
		n = int(raw_input())
	except:
		break

	l = fat(n)
	num = "numeros"
	if n == 0:
		num = "numero"
	print "Caso %d: %d %s" %(tot,  len(l) , num)
	tot += 1
	for i in l:
		print i,

	