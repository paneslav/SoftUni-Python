def separate_positive_negative(numbers):
    for num in numbers:
        if num < 0:
            negative_numbers.append(num)
        else:
            positive_numbers.append(num)


positive_numbers = []
negative_numbers = []

numbers = [int(x) for x in input().split()]

separate_positive_negative(numbers)
negative_sum = sum(negative_numbers)
positive_sum = sum(positive_numbers)

print(negative_sum)
print(positive_sum)
if abs(negative_sum) > abs(positive_sum):
    print(f"The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

