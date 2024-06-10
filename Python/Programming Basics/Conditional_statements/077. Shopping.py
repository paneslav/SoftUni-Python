budget = float(input())
gpuCount = int(input())
cpuCount = int(input())
ramCount = int(input())

totalSum = (gpuCount*250) + ((gpuCount*250) * 0.35 * cpuCount) + ((gpuCount*250) * 0.1 * ramCount)

if gpuCount > cpuCount:
    totalSum *= .85

if budget >= totalSum:
    print(f"You have {budget-totalSum:.2f} leva left!")
else:
    print(f"Not enough money! You need {totalSum-budget:.2f} leva more!")

                                                                  