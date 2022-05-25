import math

hoursNeeded = int(input())
daysToFinish = int(input())
overtimeWorkers = int(input())

training = daysToFinish * 0.1
totalTime = math.floor((daysToFinish-training) * 8 + (overtimeWorkers*2*daysToFinish))

if totalTime >= hoursNeeded:
    print(f"Yes!{(totalTime-hoursNeeded)} hours left.")
else:
    print(f"Not enough time!{(abs(totalTime-hoursNeeded))} hours needed.")

