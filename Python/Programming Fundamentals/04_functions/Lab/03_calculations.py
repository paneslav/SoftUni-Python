def calculations(operation, number_1, number_2):
    if operation == "multiply":
        print(number_1 * number_2)
    elif operation == "divide":
        print(int(number_1/number_2))
    elif operation == "add":
        print(number_1+number_2)
    elif operation == "subtract":
        print(number_1 - number_2)


operator = input()
a = int(input())
b = int(input())

calculations(operator, a, b)