def fCompleta(words):
	conta=0
	alpha=map(chr, range(ord("a"), (ord("z")+1))) 
	for i in alpha:
		for j in words:
			if i.lower() == j.lower():
				conta+=1
				break

	if conta==len(alpha):
		print "frase completa"
	elif conta>=len(alpha)/2:
		print "frase quase completa"
	else:
		print "frase mal elaborada"

n=int(input())
for x in range(n):
	fCompleta(raw_input())