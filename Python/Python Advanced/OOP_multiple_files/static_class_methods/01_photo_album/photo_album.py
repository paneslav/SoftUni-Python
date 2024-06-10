import math
from math import ceil


class PhotoAlbum():
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]  # 4 photos per page

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.ceil(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for index in range(len(self.photos)):
            if len(self.photos[index]) < 4:
                self.photos[index].append(label)
                return f"{label} photo added successfully on page {index + 1} slot {len(self.photos[index])}"

        return f"No more free slots"

    def display(self):
        dashes = '-----------'
        result = [dashes]
        for page in self.photos:
            result.append('[] ' * len(page))
            result.append(dashes)

        return '\n'.join([l.strip() for l in result])


album = PhotoAlbum(2)
album2 = PhotoAlbum.from_photos_count(5)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
print(album2.display())