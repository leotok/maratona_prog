# https://www.urionlinejudge.com.br/judge/pt/problems/view/1030

import sys
sys.setrecursionlimit(10500)

def josephus(n, m):
    if n == 1:
        return 1
    return ((josephus(n-1, m) + m - 1) % n) + 1

k = int(input())

for i in range(k):
    n, m = map(long, raw_input().split())

    print "Case %d: %d" % (i+1, josephus(n, m))