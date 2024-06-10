country = input().split(', ')
capitals = input().split(', ')

zipped_dict = dict(zip(country, capitals))
result_to_print = [f'{item} -> {zipped_dict[item]}' for item in zipped_dict]
print(f"\n".join(result_to_print))