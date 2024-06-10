def concatenate(*args, **kwargs):
    result = ''
    for word in args:
        result += word

    for key, value in kwargs.items():
        if key in result:
            result = result.replace(key, value)

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))





# def func_executor(*args):
#     result = ''
#     for item in args:
#         func = item[0](item[1])
#         print(f'{item[0]} - {func}')
#
# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result
#
# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result
#
# print(func_executor(
#     (make_upper, ("Python", "softUni")),
#     (make_lower, ("PyThOn",)),
# ))