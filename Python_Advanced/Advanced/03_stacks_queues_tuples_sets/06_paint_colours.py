from collections import deque


def check_orange(collected_colors):
    if 'red' in collected_colors and 'yellow' in collected_colors:
        final_colors.append('orange')


def check_purple(collected_colors):
    if 'red' in collected_colors and 'blue' in collected_colors:
        final_colors.append('purple')


def check_green(collected_colors):
    if 'yellow' in collected_colors and 'blue' in collected_colors:
        final_colors.append('green')


colors = deque([x for x in input().split()])  # d yel blu e low redd

main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']

collected_colors = []

while colors:
    first = colors.popleft()
    last = colors.pop() if colors else ''

    if first + last in main_colors or first + last in secondary_colors:
        collected_colors.append(first + last)
    elif last + first in main_colors or last + first in secondary_colors:
        collected_colors.append(last + first)
    else:
        first = first[:-1]
        last = last[:-1]

        if first:
            colors.insert(len(colors) // 2, first)

        if last:
            colors.insert(len(colors) // 2, last)

final_colors = []

requirements = {
    'orange': check_orange,
    'purple': check_purple,
    'green': check_green
}

for color in collected_colors:
    if color in main_colors:
        final_colors.append(color)
        continue

    if color in secondary_colors:
        add_or_not = requirements[color](collected_colors)

print(final_colors)