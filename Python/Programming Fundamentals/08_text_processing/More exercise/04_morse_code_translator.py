morse_code = [x.split(' ') for x in input().split(' | ')]

decrypted_msg = ''

code_dict = {'.-': 'A',
             '-...': 'B',
             '-.-.': 'C',
             '-..': 'D',
             '.': 'E',
             '..-.': 'F',
             '--.': 'G',
             '....': 'H',
             '..': 'I',
             '.---': 'J',
             '-.-': 'K',
             '.-..': 'L',
             '--': 'M',
             '-.': 'N',
             '---': 'O',
             '.--.': 'P',
             '--.-': 'Q',
             '.-.': 'R',
             '...': 'S',
             '-': 'T',
             '..-': 'U',
             '...-': 'V',
             '.--': 'W',
             '-..-': 'X',
             '-.--': 'Y',
             '--..': 'Z',
             }

for nested_list in morse_code:
    for item in nested_list:
        if item not in code_dict:
            continue
        decrypted_msg += code_dict[item]
    decrypted_msg += ' '

print(decrypted_msg.strip())