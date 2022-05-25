skumriqPrice = float(input())
cacaPrice = float(input())
palamudKG = float(input())
safridKG = float(input())
midiKG = float(input())

midiTotal = midiKG * 7.50
safridTotal = safridKG * (cacaPrice + (cacaPrice * 0.8))
palamudTotal = palamudKG * (skumriqPrice + (skumriqPrice * 0.6))

totalSum = midiTotal + safridTotal + palamudTotal

print(f"{totalSum:.2f}")