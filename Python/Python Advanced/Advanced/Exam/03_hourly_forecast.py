def forecast(*args):
    result = ''
    weather_dict = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    for item in args:
        location = item[0]
        weather = item[-1]

        weather_dict[weather].append(location)

    for key, value in weather_dict.items():
        for item in sorted(value):
            result += f'{item} - {key}' + '\n'

    return result

print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))