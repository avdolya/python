from itertools import product


def main():
    ...


operations = {
    'not': 'not',
    'and': 'and',
    'or': 'or',
    '^': '!=',
    '->': '<=',
    '~': '==',
}

priority = {
    'not': 0,
    'and': 1,
    'or': 2,
    '^': 3,
    '->': 4,
    '~': 5,
    '(': 6,
}
def pol_kalk(a, res):
    stack = []
    result = []
    a = a.replace(')', ' )').replace('(','( ')
    for i in a.split():
        if i in res:
            result.append(i)
        elif i == '(':
            stack.append(i)
        elif i in operations:
            while stack and priority[i] >= priority[stack[-1]]:
                result.append(operations[stack.pop()])
            stack.append(i)
        elif i == ')':
            while stack[-1] != '(':
                result.append(operations[stack.pop()])
            stack.pop()
    while stack:
        result.append(operations[stack.pop()])
    return result
def ev(a, res):
    stack = []
    for i in a:
        if i in res:
            stack.append(res[i])
        else:
            if i == 'not':
                stack.append(not stack.pop())
            if i != 'not':
                v2, v1 = stack.pop(), stack.pop()
                stack.append(eval(f'{v1} {i} {v2}'))
                
                
    return int(stack.pop())
                    
                
                
a = input()
s = set()
for i in a:
    if i.isupper():
        s.add(i)
res = sorted(list(s))
print(' '.join(res) + ' F')
pol_kalk_1 = pol_kalk(a, res)
t = product([0, 1], repeat=len(res))
for i in t:
    globals = {key: j for key, j in zip(res, i)}
    print(*i, ev(pol_kalk_1, globals))
if __name__ == "__main__":
    main()