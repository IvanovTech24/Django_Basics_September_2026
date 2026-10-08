from datetime import date

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from pets.models import Pet
from photos.models import Photo


class Command(BaseCommand):
    help = 'Populate the Pet and Photo tables with meaningful sample records.'

    PETS = [
        {
            'name': 'Milo',
            'personal_photo': 'https://images.unsplash.com/photo-1552053831-71594a27632d',
            'date_of_birth': date(2021, 5, 14),
        },
        {
            'name': 'Luna',
            'personal_photo': 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba',
            'date_of_birth': date(2020, 9, 2),
        },
        {
            'name': 'Bucky',
            'personal_photo': 'https://images.unsplash.com/photo-1543466835-00a7907e9de1',
            'date_of_birth': date(2019, 12, 21),
        },
        {
            'name': 'Nala',
            'personal_photo': 'https://images.unsplash.com/photo-1574158622682-e40e69881006',
            'date_of_birth': date(2022, 3, 8),
        },
        {
            'name': 'Rocky',
            'personal_photo': 'https://images.unsplash.com/photo-1583511655826-05700442b31b',
            'date_of_birth': date(2018, 7, 30),
        },
        {
            'name': 'Coco',
            'personal_photo': 'https://images.unsplash.com/photo-1543852786-1cf6624b9987',
            'date_of_birth': date(2021, 11, 5),
        },
        {
            'name': 'Sasho',
            'personal_photo': 'https://images.unsplash.com/photo-1522069169874-c58ec4b76be5',
            'date_of_birth': date(2023, 1, 17),
        },
        {
            'name': 'Bella',
            'personal_photo': 'https://images.unsplash.com/photo-1560807707-8cc77767d783',
            'date_of_birth': date(2020, 4, 24),
        },
        {
            'name': 'Oscar',
            'personal_photo': 'https://images.unsplash.com/photo-1592194996308-7b43878e84a6',
            'date_of_birth': date(2019, 6, 11),
        },
        {
            'name': 'Ziggy',
            'personal_photo': 'https://images.unsplash.com/photo-1548767797-d8c844163c4c',
            'date_of_birth': date(2022, 10, 3),
        },
    ]

    PHOTOS = [
        {
            'photo': 'images/dog-on-road.jpg',
            'description': 'Bucky enjoying a bright morning walk in the park.',
            'location': 'Sofia, Bulgaria',
            'tagged_pets': ['Bucky'],
        },
        {
            'photo': 'images/dog-on-bed.jpg',
            'description': 'Bella claimed the soft blanket after a long play session.',
            'location': 'Plovdiv, Bulgaria',
            'tagged_pets': ['Bella'],
        },
        {
            'photo': 'images/axolotl.jpeg',
            'description': 'Sasho exploring the plants in his freshly cleaned tank.',
            'location': 'Varna, Bulgaria',
            'tagged_pets': ['Sasho'],
        },
        {
            'photo': 'images/dog-on-road.jpg',
            'description': 'Milo and Rocky waiting patiently for their favorite treats.',
            'location': 'Bansko, Bulgaria',
            'tagged_pets': ['Milo', 'Rocky'],
        },
        {
            'photo': 'images/dog-on-bed.jpg',
            'description': 'Luna supervising Sunday reading from the warmest pillow.',
            'location': 'Burgas, Bulgaria',
            'tagged_pets': ['Luna'],
        },
        {
            'photo': 'images/axolotl.jpeg',
            'description': 'Coco inspecting the camera with maximum curiosity.',
            'location': 'Ruse, Bulgaria',
            'tagged_pets': ['Coco'],
        },
        {
            'photo': 'images/dog-on-road.jpg',
            'description': 'Nala found the perfect sunny spot beside the garden path.',
            'location': 'Veliko Tarnovo',
            'tagged_pets': ['Nala'],
        },
        {
            'photo': 'images/dog-on-bed.jpg',
            'description': 'Oscar practicing his serious portrait face before dinner.',
            'location': 'Dobrich, Bulgaria',
            'tagged_pets': ['Oscar'],
        },
        {
            'photo': 'images/axolotl.jpeg',
            'description': 'Ziggy making a splash during afternoon tank maintenance.',
            'location': 'Pleven, Bulgaria',
            'tagged_pets': ['Ziggy'],
        },
        {
            'photo': 'images/dog-on-road.jpg',
            'description': 'Milo, Luna, and Bella posing together after training class.',
            'location': 'Stara Zagora',
            'tagged_pets': ['Milo', 'Luna', 'Bella'],
        },
    ]

    def handle(self, *args, **options):
        pets_by_name = {}

        for pet_data in self.PETS:
            slug = slugify(f'{pet_data["name"]}-seed')
            pet, _ = Pet.objects.update_or_create(
                slug=slug,
                defaults={
                    'name': pet_data['name'],
                    'personal_photo': pet_data['personal_photo'],
                    'date_of_birth': pet_data['date_of_birth'],
                },
            )

            if pet.slug != slug:
                pet.slug = slug
                pet.save(update_fields=['slug'])

            pets_by_name[pet.name] = pet

        for photo_data in self.PHOTOS:
            photo, _ = Photo.objects.update_or_create(
                description=photo_data['description'],
                defaults={
                    'photo': photo_data['photo'],
                    'location': photo_data['location'],
                },
            )
            photo.tagged_pets.set(
                pets_by_name[name]
                for name in photo_data['tagged_pets']
            )

        self.stdout.write(
            self.style.SUCCESS(
                f'Seeded {len(self.PETS)} pets and {len(self.PHOTOS)} photos.'
            )
        )
