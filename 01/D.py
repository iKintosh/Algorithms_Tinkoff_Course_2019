def detect_right_brakets(brackets):
    opened = ['(', '[', '{']
    closed = [')', ']', '}']
    stack = []
    for symbol in brackets:
        if symbol in opened:
            stack.append(symbol)

        if symbol in closed:
            if len(stack) == 0:
                return 'NO'
            elif closed.index(symbol) != opened.index(stack.pop()):
                return 'NO'

    if len(stack) != 0:
        return 'NO'
    return 'YES'


brackets = input()
answ = detect_right_brakets(brackets)
print(answ)