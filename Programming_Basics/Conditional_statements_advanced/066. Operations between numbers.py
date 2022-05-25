n1 = int(input())
n2 = int(input())
operator = input()

result = 0

if operator == "+":
    print(f"{n1} + {n2} = {n1+n2} - {'even' if (n1+n2)%2==0 else 'odd'}")
elif operator == "-":
    print(f"{n1} - {n2} = {n1 - n2} - {'even' if (n1-n2)%2==0 else 'odd'}")
elif operator == "*":
    print(f"{n1} * {n2} = {n1 * n2} - {'even' if (n1*n2)%2==0 else 'odd'}")
elif operator == "/" and n2 != 0:
    print(f"{n1} / {n2} = {n1 / n2:.2f}")
elif operator == "%" and n2 != 0:
    print(f"{n1} % {n2} = {n1 % n2}")
else:
    print(f"Cannot divide {n1} by zero")