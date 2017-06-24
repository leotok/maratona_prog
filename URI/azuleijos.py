# https://www.urionlinejudge.com.br/judge/pt/problems/view/1512

def mmc(num1, num2):
    a = num1
    b = num2

    resto = None
    while resto is not 0:
        resto = a % b
        a  = b
        b  = resto

    return (num1 * num2) / a

def n(an,a1,r):
	return ((an-a1)/r)+1

def azuleijos(a, b, c):
	print "%d" %(n(a,b,b)+n(a,c,c)-n(a,mmc(b,c),mmc(b, c))) 

while True:
	a,b,c=map(int,raw_input().split())
	if a==b==c==0:
		break
	azuleijos(a, b, c)