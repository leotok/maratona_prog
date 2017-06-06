# https://www.urionlinejudge.com.br/judge/pt/questions/view/1220/215

while True:

	n = int(raw_input())

	if n == 0:
		break

	total = 0.0
	maximo = -1
	minimo = 20000

	valores = []

	for _ in xrange(n):
		din = int(float(raw_input()) * 1000/10)

		total += din
		valores.append(din)

	final = float(total) / n

	maior = 0
	menor = 0

	for v in valores:
		if v > final:
			maior += int(v - final) / 100.0
		else:
			menor += int(final - v) / 100.0

	if menor > maior:
		print "$%.2f" % float(menor)
	else:
		print "$%.2f" % float(maior)

	