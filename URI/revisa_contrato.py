# https://www.urionlinejudge.com.br/judge/pt/problems/view/1120

while True:

	read = raw_input().split(" ")
	falha = read[0]
	num = read[1]

	if falha == "0" and num == "0":
		break

	num = num.replace(falha, "")
	print int(num) if num != "" else "0"
