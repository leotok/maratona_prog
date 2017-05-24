#!/bin/python

import sys
import operator

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
    
first_diagonal = [x[i] for i, x in enumerate(a)]
second_diagonal = [x[n - 1 - i] for i, x in enumerate(a)]

print abs(reduce(operator.add, first_diagonal) - reduce(operator.add, second_diagonal))

