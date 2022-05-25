examHour = int(input())
examMinute = int(input())
arrivalHour = int(input())
arrivalMinute = int(input())

hours = 0
minutes = 0

examMinutes = examHour * 60 + examMinute
arrivalMinutes = arrivalHour * 60 + arrivalMinute
difference = abs(examMinutes-arrivalMinutes)

if difference <= 30:
    print("On time")
    if difference != 0:
        print(f"{difference} minutes before the start")
if arrivalMinutes > examMinutes:
    print("Late")
    if difference <= 59:
        print(f"{difference} minutes after the start")
    elif difference > 59:
        if difference % 60 < 10:
            print(f"{difference//60}:0{difference%60} hours after the start")
        else:
            print(f"{difference // 60}:{difference % 60} hours after the start")
else:
    print("Early")
    if difference <= 59:
        print(f"{difference} minutes before the start")
    elif difference > 59:
        if difference % 60 < 10:
            print(f"{difference//60}:0{difference%60} hours before the start")
        else:
            print(f"{difference // 60}:{difference % 60} hours before the start")