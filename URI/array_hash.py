# https://www.urionlinejudge.com.br/judge/en/problems/view/1257

def array_hash(ls):
	cl = 0
	tot = 0
	for l in ls:
		for i in range(len(l)):
			tot += (ord(l[i]) - 65) + cl + i
		cl += 1
	return tot

t = int(raw_input())
for i in range(t):
	l = int(raw_input())
	ls = []
	for j in range(l):
		ls.append(raw_input())
	print(array_hash(ls))
	ls = []