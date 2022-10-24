from os import linesep


def start_spring(**kwargs):
    result = ''
    objects_collection = {}

    for key, value in kwargs.items():
        objects_collection[value] = objects_collection.get(value, [])
        objects_collection[value].append(key)

    for key, value in sorted(objects_collection.items(), key=lambda x: (-len(x[1]), x[0])):
        result += f'{key}:' + linesep
        for item in sorted(value):
            result += f'-{item}' + linesep

    return result


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))

example_objects = {"Swallow": "bird",
                   "Thrushes": "bird",
                   "Woodpeckers": "bird",
                   "Swallows": "bird",
                   "Warblers": "bird",
                   "Shrikes": "bird", }
print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
