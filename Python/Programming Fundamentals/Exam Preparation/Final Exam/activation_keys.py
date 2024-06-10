raw_key = input()

while True:
    operation = input().split('>>>')

    if operation[0] == 'Generate':
        print(f'Your activation key is: {raw_key}')
        break

    if operation[0] == 'Contains':
        wanted_string = operation[1]
        if wanted_string in raw_key:
            print(f'{raw_key} contains {wanted_string}')
        else:
            print(f'Substring not found!')

    elif operation[0] == 'Flip':
        start_index = int(operation[2])
        end_index = int(operation[-1])
        upper_or_lower = operation[1]
        if upper_or_lower == 'Upper':
            raw_key = raw_key[:start_index] + raw_key[start_index:end_index].upper() + raw_key[end_index:]
        else:
            raw_key = raw_key[:start_index] + raw_key[start_index:end_index].lower() + raw_key[end_index:]
        print(raw_key)

    elif operation[0] == 'Slice':
        start_index = int(operation[1])
        end_index = int(operation[-1])
        raw_key = raw_key[:start_index] + raw_key[end_index:]
        print(raw_key)