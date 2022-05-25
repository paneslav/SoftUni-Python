import math

record = float(input())
distance = float(input())
timePerMeter = float(input())

resistance = math.floor(distance/15) * 12.5

timeToSwim = timePerMeter * distance + resistance

if timeToSwim < record:
    print(f"Yes, he succeeded! The new world record is {timeToSwim:.2f} seconds.")
else:
    print(f"No, he failed! He was {timeToSwim-record:.2f} seconds slower.")