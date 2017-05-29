# https://www.urionlinejudge.com.br/judge/pt/problems/view/1077
from collections import deque


def isOperand(operando):
    operando = unicode(operando, 'utf-8')
    if(operando.isalpha() or operando.isnumeric()):
        return True
    return False

def isEmpty(stack):
    if len(stack)==0:
        return True
    return False

n = int(raw_input())

while n:
    n -= 1

    order = {
        '(': 3,
        '^': 3,
        '*': 2,
        '/': 2,
        '+': 1,
        '-': 1
    }

    post_fix = []
    equation = raw_input()

    op_stack = deque()

    for i in xrange(len(equation)):
        if isOperand(equation[i]):
            post_fix.append(equation[i])
        elif equation[i] == '(':
            op_stack.append(equation[i])
        elif equation[i] == ')':
            top_op = op_stack.pop()
            while top_op != '(':
                post_fix.append(top_op)
                if op_stack:
                    top_op = op_stack.pop()
                else:
                    break
        else:
            while not isEmpty(op_stack) and order[op_stack[-1]] >= order[equation[i]]:
                op = op_stack.pop()
                if op not in ['(', ')']:
                    post_fix.append(op)
            op_stack.append(equation[i])

    while not isEmpty(op_stack):
        post_fix.append(op_stack.pop())

    print "".join(post_fix)