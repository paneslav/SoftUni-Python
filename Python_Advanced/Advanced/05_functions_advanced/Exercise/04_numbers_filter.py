def even_odd_filter(**kwargs):
    md = {}
    result = {}
    for key, value in kwargs.items():
        if key == 'even':
            md[key] = [x for x in value if x % 2 == 0]
        else:
            md[key] = [x for x in value if x % 2 != 0]

    sorted_dict = sorted(md.items(), key=lambda x: -len(x[1]))

    for key, value in sorted_dict:
        result[key] = value

    return result

print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))