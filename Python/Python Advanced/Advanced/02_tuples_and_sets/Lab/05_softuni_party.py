number_of_guests = int(input())

vip_guests = set()
normal_guests = set()

for i in range(number_of_guests):
    invitation = input()

    if invitation[0].isdigit():
        vip_guests.add(invitation)
    else:
        normal_guests.add(invitation)


while True:
    invitation = input()

    if invitation == 'END':
        break

    if invitation in vip_guests:
        vip_guests.remove(invitation)
    elif invitation in normal_guests:
        normal_guests.remove(invitation)

print(len(vip_guests) + len(normal_guests))
[print(inv) for inv in sorted(vip_guests)]
[print(inv) for inv in sorted(normal_guests)]