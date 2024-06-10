from collections import deque


def math_operations(*args, **kwargs):
    positions = deque([1, 2, 3, 4])
    result = ''

    for idx in range(len(args)):
        current_position = positions.popleft()
        if current_position == 1:
            kwargs['a'] += args[idx]

        elif current_position == 2:
            kwargs['s'] -= args[idx]

        elif current_position == 3:
            key_value = kwargs['d']
            if key_value <= 0 or args[idx] <= 0:
                continue
            kwargs['d'] = key_value / args[idx]

        elif current_position == 4:
            kwargs['m'] *= args[idx]
        positions.append(current_position)

    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result += f'{key}: {value:.1f}\n'

    return result

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
