def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def make_possible_calc(s):
    result = []
    for i, j in enumerate(s):
        if j in operands and i >= 2:
            try:
                a = int(s[i-2])
                b = int(s[i-1])
                result.append(operands[j](a,b))
            except:
                result.append(j)
        if j not in operands:
            if s[i+1] in operands and s[i-1] not in operands:
                continue
            elif s[i+1] in operands and s[i-1] in operands:
                result.append(j)
            elif s[i+1] not in operands and s[i+2] not in operands:
                result.append(j)
            else:
                continue
    return result

operands = {'+': add,
            '-': sub,
            '*': mul}

string = input().split()
while (('+' in string) or ('-' in string) or ('*' in string)):
    string = make_possible_calc(string)
print(string[0])