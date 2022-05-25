first_match = input()
second_match = input()
third_match = input()

win = 0
loss = 0
draw = 0

if int(first_match[0]) > int(first_match[2]):
    win += 1
elif int(first_match[0]) < int(first_match[2]):
    loss += 1
else:
    draw += 1

if int(second_match[0]) > int(second_match[2]):
    win += 1
elif int(second_match[0]) < int(second_match[2]):
    loss += 1
else:
    draw += 1

if int(third_match[0]) > int(third_match[2]):
    win += 1
elif int(third_match[0]) < int(third_match[2]):
    loss += 1
else:
    draw += 1

print(f"Team won {win} games.")
print(f"Team lost {loss} games.")
print(f"Drawn games: {draw}")