number = int(input())

isPrime = True

counter = 0

for i in range(2, number):

    if number % i == 0:
        isPrime = False
        break

print(isPrime)
