def maior_ab(a, b):
	return (a + b + abs(a - b)) / 2

a, b, c = map(int,raw_input().split())

maior = maior_ab(a, b)
maior = maior_ab(c, maior)

print "%d eh o maior" %(maior)
