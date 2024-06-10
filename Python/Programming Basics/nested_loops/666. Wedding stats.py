sector = input()
row_count = int(input())
seats_per_odd = int(input())

first_record = seats_per_odd
sector_count = 0

seats_count = 0

start = 'a'


for i in range(ord('A'), ord(sector) + 1):
    for x in range(1, row_count + 1):
        if x % 2 == 0:
            seats_per_odd += 2
        for y in range(ord(start), ord(start) + seats_per_odd):
            print(f"{chr(i)}{x}{chr(y)}")
            seats_count += 1

        seats_per_odd = first_record

    row_count += 1

print(seats_count)