def operate(operator, *args):
    def add():
        return sum(args)

    def substract():
        start = args[0]
        for item in args[1:]:
            start -= item
        return start

    def multiply():
        start = args[0]
        for item in args[1:]:
            start *= item
        return start

    def divide():
        start = args[0]
        for item in args[1:]:
            start /= item
        return start

    if operator == '+':
        return add()
    elif operator == '*':
        return multiply()
    elif operator == '/':
        return divide()
    elif operator == '-':
        return substract()


print(operate("+", 1, 2, 3))
print(operate("/", 0, 3, 4))
