def age_assignment(*args, **kwargs):
    result = ''

    for person in sorted(args):
        result += f'{person} is {kwargs[person[0]]} years old.\n'

    return result



print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))