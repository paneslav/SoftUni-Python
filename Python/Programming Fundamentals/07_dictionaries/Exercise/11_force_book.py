def assign_side(side, user):
    if any(user in val for val in forces_dict.values()):
        return
    if side not in forces_dict:
        forces_dict[side] = []
    forces_dict[side].append(user)


def change_side(user, side):
    for key, value in forces_dict.items():
        if user in value:
            # forces_dict[key].remove(user)
            if side not in forces_dict:
                forces_dict[side] = []
            forces_dict[side].append(forces_dict[key].pop(forces_dict[key].index(user)))
            return
    if user not in forces_dict.values() and side in forces_dict:
        forces_dict[side].append(user)
        return

    forces_dict[side] = []
    forces_dict[side].append(user)


forces_dict = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break

    if '|' in command:
        command = command.split(' | ')
        force_side = command[0]
        force_user = command[-1]
        assign_side(force_side, force_user)

    elif '->' in command:
        command = command.split(' -> ')
        force_user = command[0]
        force_side = command[-1]
        change_side(force_user, force_side)
        print(f"{force_user} joins the {force_side} side!")


for side in forces_dict:
    if len(forces_dict[side]) > 0:
        members = [f'! {member}' for member in forces_dict[side]]
        print(f"Side: {side}, Members: {len(forces_dict[side])}")
        print('\n'.join(members))
