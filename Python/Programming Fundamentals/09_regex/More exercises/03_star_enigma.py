import re

n = int(input())
pattern = r'[^\@\-\!\:\>]*?@([a-zA-Z]+)[^\@\-\!\:\>]*?:(\d+)[^\@\-\!\:\>]*?!([A-Z])![^\@\-\!\:\>]*?->(\d+)'
chars_to_search = ['s', 't', 'a', 'r']

attacked_planets = []
destroyed_planets = []

for i in range(n):
    decryption_key = 0
    decrypted_msg = ''

    command = input()

    for char in command:
        if char.lower() in chars_to_search:
            decryption_key += 1
    for char in command:
        decrypted_msg += chr(ord(char) - decryption_key)

    match = re.search(pattern, decrypted_msg)

    if match:
        planet_name, planet_population, attack_type, soldier_count = match.groups()
        if attack_type == 'A':
            attacked_planets.append(planet_name)
        else:
            destroyed_planets.append(planet_name)

print(f'Attacked planets: {len(attacked_planets)}')
for planet in sorted(attacked_planets):
    print(f"-> {planet}")
print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")