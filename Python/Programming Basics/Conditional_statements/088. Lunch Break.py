import math

seriesName = input()
seriesLenght = int(input())
breakLenght = int(input())

lunchTime = breakLenght * 1/8
breakTime = breakLenght * 1/4

timeLeft = abs(breakLenght - lunchTime - breakTime)


if timeLeft >= seriesLenght:
    print(f"You have enough time to watch {seriesName} and left with {math.ceil(timeLeft-seriesLenght)} minutes free time.")
else:
    print(f"You don't have enough time to watch {seriesName}, you need {math.ceil(seriesLenght-timeLeft)} more minutes.")