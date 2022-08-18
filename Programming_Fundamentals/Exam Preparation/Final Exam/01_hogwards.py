spell = input()

while True:
    command = input().split()
    if command[0] == 'Abracadabra':
        break

    action = command[0]

    if action == 'Abjuration':
        spell = spell.upper()
        print(spell)
    elif action == 'Necromancy':
        spell = spell.lower()
        print(spell)
    elif action == 'Illusion':
        index_to_replace = int(command[1])
        replacement = command[-1]

        if index_to_replace < len(spell):
            spell = spell[:index_to_replace] + replacement + spell[index_to_replace + 1:]
            print(f"Done!")
        else:
            print(f"The spell was too weak.")
    elif action == 'Divination':
        first_string = command[1]
        replacement = command[-1]

        if first_string in spell:
            spell = spell.replace(first_string, replacement)
            print(spell)
    elif action == 'Alteration':
        string_to_remove = command[1]
        if string_to_remove in spell:
            spell = spell.replace(string_to_remove, '')
            print(spell)
    else:
        print("The spell did not work!")