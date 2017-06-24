def justyII(l):
	k=[]
	for x in l:
		k.append(" ".join(x))

	m=max(map(len, k))
	for x in k:
		if len(x) != m:
			marginL = (m - len(x))
			print "%s%s" %(marginL*" ", x)
		else:
			print "%s" %x

flag=0
while True:
	n,L=int(input()), []
	if n == 0:
		break
	if flag == 1: 
		print;
	for x in range(n):
		L.append(raw_input().split())
	justyII(L)
	flag=1