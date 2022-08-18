def cast_spell(char_info, char_name, mp_needed, spell_name):
    if char_info[char_name]['mp'] >= mp_needed:
        char_info[char_name]['mp'] -= mp_needed
        print(f"{char_name} has successfully cast {spell_name} and now has {char_info[char_name]['mp']} MP!")
    else:
        print(f"{char_name} does not have enough MP to cast {spell_name}!")


def take_damage(char_info, char_name, damage, attacker):
    if char_info[char_name]['hp'] > damage:
        char_info[char_name]['hp'] -= damage
        print(f"{char_name} was hit for {damage} HP by {attacker} and now has {char_info[char_name]['hp']} HP left!")
    else:
        print(f"{char_name} has been killed by {attacker}!")
        del char_info[char_name]


def recharge_mp(char_info, char_name, amount):
    if char_info[char_name]['mp'] + amount <= 200:
        char_info[char_name]['mp'] += amount
        print(f"{char_name} recharged for {amount} MP!")
    else:
        print(f"{char_name} recharged for {200 - char_info[char_name]['mp']} MP!")
        char_info[char_name]['mp'] = 200


def heal(char_info, char_name, amount):
    if char_info[char_name]['hp'] + amount <= 100:
        char_info[char_name]['hp'] += amount
        print(f"{char_name} healed for {amount} HP!")
    else:
        print(f"{char_name} healed for {100 - char_info[char_name]['hp']} HP!")
        char_info[char_name]['hp'] = 100


n = int(input())

char_info = {}

for i in range(n):
    character_name, hp, mp = input().split()
    char_info[character_name] = {'hp': int(hp), 'mp': int(mp)}

while True:
    command = input().split(' - ')

    if command[0] == 'End':
        break

    char_name = command[1]
    action = command[0]

    if action == 'CastSpell':
        mp_needed = int(command[2])
        spell_name = command[-1]
        cast_spell(char_info, char_name, mp_needed, spell_name)

    elif action == 'TakeDamage':
        damage = int(command[2])
        attacker = command[-1]
        take_damage(char_info, char_name, damage, attacker)

    elif action == 'Recharge':
        amount = int(command[-1])
        recharge_mp(char_info, char_name, amount)

    elif action == 'Heal':
        amount = int(command[-1])
        heal(char_info, char_name, amount)


for char in char_info:
    print(f"{char}")
    print(f"  HP: {char_info[char]['hp']}")
    print(f"  MP: {char_info[char]['mp']}")