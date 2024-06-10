def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * length + 2 * width

    if type(length) != int or type(width) != int:
        return f'Enter valid values!'

    return f'Rectangle area: {area()}\n' \
           f'Rectangle perimeter: {perimeter()}'


print(rectangle(2, 10))
print(rectangle('2', 10))
