# https://www.urionlinejudge.com.br/judge/pt/problems/view/2456

a, b, c, d, e = map(int, raw_input().split())

C = a < b < c < d < e
D = a > b > c > d > e

if C:
	print 'C'
elif D:
	print 'D'
else:
	print 'N'
