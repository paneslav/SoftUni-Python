pencils = int(input()) * 5.80
markers = int(input()) * 7.20
chemicals = int(input()) * 1.20
discount = int(input())

sum = pencils+markers+chemicals
totalSum = sum -(sum * (discount/100))


print(totalSum)



