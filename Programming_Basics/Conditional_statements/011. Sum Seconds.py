first = int(input())
second = int(input())
third = int(input())

secondsSum = first + second + third
minutes = secondsSum // 60
seconds = secondsSum % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")