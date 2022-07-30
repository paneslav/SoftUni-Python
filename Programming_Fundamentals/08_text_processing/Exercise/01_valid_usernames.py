# usernames = input().split(', ')
# valid_usernames = []
# allowed_symbols = ['-', '_']
#
# for user in usernames:
#     if 3 <= len(user) <= 16:
#         if user.isalnum():
#             valid_usernames.append(user)
#         else:
#             for symbol in allowed_symbols:
#                 if symbol in user:
#                     valid_usernames.append(user)
#
# print('\n'.join(valid_usernames))

import re

usernames = input().split(', ')
valid_usernames = []

for user in usernames:
    if re.match("^[A-Za-z0-9_-]*$", user) and 3 <= len(user) <= 16:
        valid_usernames.append(user)

print('\n'.join(valid_usernames))
