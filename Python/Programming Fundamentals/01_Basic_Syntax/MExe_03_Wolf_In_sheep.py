string = input()

queue = string.split(", ")
queue.reverse()

wolf_position = queue.index('wolf')

if queue[0] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {wolf_position}! You are about to be eaten by a wolf!")