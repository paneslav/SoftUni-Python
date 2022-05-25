hours = int(input())
minutes = int(input())

totalSeconds = hours*3600 + minutes*60
timeIn15 = totalSeconds + (15*60)

hoursIn15 = timeIn15 // 3600
minuteIn15 = (timeIn15 % 3600) // 60


if hoursIn15>23:
    hoursIn15 = 0

if minuteIn15 < 10:
    print(f"{hoursIn15}:0{minuteIn15}")
else:
    print(f"{hoursIn15}:{minuteIn15}")


