freeDays = int(input())

workingsDays = 365 - freeDays

totalPlayTime = (freeDays*127) + workingsDays * 63
difference = abs(30000-totalPlayTime)

if totalPlayTime < 30000:
    print(f"Tom sleeps well")
    print(f"{difference//60} hours and {difference%60} minutes less for play")
else:
    print("Tom will run away")
    print(f"{difference//60} hours and {difference%60} minutes more for play")