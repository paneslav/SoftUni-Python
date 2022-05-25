import math

totalPages = int(input())
pages_per_hour = int(input())
days = int(input())

hours = totalPages // pages_per_hour
hoursPerDay = hours // days

print(hoursPerDay)
