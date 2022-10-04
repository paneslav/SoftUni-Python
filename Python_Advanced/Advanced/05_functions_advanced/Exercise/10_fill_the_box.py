def fill_the_box(h, l, w, *args):
    box_size = h * l * w

    for item in args:
        if item == 'Finish':
            break

        box_size -= item

    if box_size > 0:
        return f'There is free space in the box. You could put {box_size} more cubes.'
    else:
        return f'No more free space! You have {abs(box_size)} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))