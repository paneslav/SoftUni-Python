import os
from datetime import timedelta, date

import django
from django.db import transaction
from django.db.models import Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

from main_app.models import *


# Create queries within functions

# 1

def show_all_authors_with_their_books() -> str:
    result = []
    authors = Author.objects.prefetch_related('books').order_by('id')

    for a in authors:
        if a.books.count() == 0:
            continue

        result.append(f"{a.name} has written - {', '.join(b.title for b in a.books.all())}!")

    return '\n'.join(result)


def delete_all_authors_without_books():
    Author.objects.filter(books__isnull=True).delete()


# 2

def add_song_to_artist(artist_name: str, song_title: str):
    song = Song.objects.get(title=song_title)
    artist = Artist.objects.get(name=artist_name)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    return Artist.objects.get(name=artist_name).songs.all().order_by('-id')


def remove_song_from_artist(artist_name: str, song_title: str):
    song = Song.objects.get(title=song_title)
    artist = Artist.objects.get(name=artist_name)

    artist.songs.remove(song)


# 3


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.get(name=product_name)

    return product.reviews.aggregate(Avg('rating'))['rating__avg']


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


# 4

def calculate_licenses_expiration_dates():
    result = []
    licences = DrivingLicense.objects.all().order_by('-license_number')

    for l in licences:
        result.append(f'License with number: {l.license_number} expires on {l.issue_date + timedelta(days=365)}!')

    return '\n'.join(result)


def get_drivers_with_expired_licenses(due_date: date):
    drivers = Driver.objects.all()
    result = []

    for d in drivers:
        if d.license.issue_date + timedelta(days=365) > due_date:
            result.append(d)

    return result

    # # Calculate the expiration date threshold
    # expiration_threshold = due_date - timedelta(days=365)
    #
    # # Filter drivers whose license issue date is before the expiration threshold
    # expired_drivers = Driver.objects.filter(license__issue_date__lt=expiration_threshold)
    #
    # return expired_drivers


# 5


def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True).first()

    car.owner = owner

    car.save()

    registration.registration_date = date.today()
    registration.car = car

    registration.save()

    return f'Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}.'