keys = list(map(int, input().split()))

locations = []

while True:
    counter = 0
    msg_to_decrypt = input()
    decrypted_msg = ''

    if msg_to_decrypt == 'find':
        break

    for i in range(len(msg_to_decrypt)):
        if counter == len(keys):
            counter = 0
        decrypted_msg += chr(ord(msg_to_decrypt[i]) - keys[counter])
        counter += 1
    locations.append(decrypted_msg)

for item in locations:
    treasure = item[item.index('&') + 1:item.index('&', item.index('&') + 1)]
    location = item[item.index('<') + 1:item.index('>')]
    print(f"Found {treasure} at {location}")



# secret_key = [int(x) for x in input().split()]
# secret_msg = input()
#
# how_long = len(secret_key)
# while secret_msg != "find":
#     secret_text = "".join([chr(ord(secret_msg[i]) - secret_key[i % how_long]) for i in range(len(secret_msg))])
#     item = secret_text.split("&")[-2]
#     location = secret_text.split("<")[-1][:-1]
#     print(f"Found {item} at {location}")
#     secret_msg = input()