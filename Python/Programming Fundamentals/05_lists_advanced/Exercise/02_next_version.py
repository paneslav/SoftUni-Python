software_version = list(map(int, input().split('.')))

if software_version[2] < 10:
    software_version[2] += 1
    if software_version[2] == 10:
        software_version[2] = 0
        software_version[1] += 1
        if software_version[1] == 10:
            software_version[1] = 0
            software_version[0] += 1

print(*software_version, sep='.')