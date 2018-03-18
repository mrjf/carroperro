#!/usr/bin/env python
"""Breeds of dogs"""

from carroperro import util


class Dogs:

    breeds = {
        'Akita': [],
        'Alaskan Malamute': ['Malamute'],
        'American Bulldog': ['Bulldog'],
        'American Pit Bull Terrier': ['Pit Bull'],
        'Australian Shepherd': [],
        'Basset Hound': [],
        'Beagle': [],
        'Belgian Malinois': ['Malinois'],
        'Bernese Mountain Dog': [],
        'Bichon Frise': [],
        'Bloodhound': [],
        'Border Collie': ['Collie'],
        'Boston Terrier': [],
        'Bullmastiff': ['Mastiff'],
        'Cane Corso': [],
        'Catahoula Leopard Dog': ['Catahoula'],
        'Chihuahua': [],
        'Chinese Shar-Pei': ['Shar-Pei'],
        'Chow Chow': [],
        'Cockapoo': [],
        'Cocker Spaniel': [],
        'Welsh Corgi': ['Corgi'],
        'Dachshund': [],
        'Dalmatian': [],
        'Doberman Pinscher': ['Dobie'],
        'English Springer Spaniel': ['Springer Spaniel'],
        'Flat-Coated Retriever': [],
        'German Shepherd Dog': ['German Shepherd'],
        'Giant Schnauzer': ['Schnauzer'],
        'Golden Retriever': [],
        'Goldendoodle': [],
        'Great Dane': [],
        'Great Pyrenees': [],
        'Greyhound': [],
        'Irish Setter': [],
        'Italian Greyhound': ['Greyhound'],
        'Jack Russell Terrier': ['Jack Russell'],
        'Labradoodle': [],
        'Labrador Retriever': ['Black Lab', 'Yellow Lab', 'Chocolate Lab'],
        'Lhasa Apso': [],
        'Maltese': [],
        'Maltipoo': [],
        'Miniature Pinscher': ['Minpin'],
        'Mutt': ['Mutt dog', 'Mixed-breed'],
        'Newfoundland': ['Newfie', 'Newfy'],
        'Norwich Terrier': [],
        'Nova Scotia Duck Tolling Retriever': ['Duck Tolling Retriever'],
        'Pekingese': [],
        'Pitbull': ['Pitty', 'Pittie'],
        'Pointer': [],
        'Pomeranian': [],
        'Poodle': [],
        'Pug': [],
        'Rat Terrier': [],
        'Rescue Dog': ['Shelter Dog', 'Pound dog'],
        'Rhodesian Ridgeback': [],
        'Rottweiler': ['Rotty', 'Rottie'],
        'Saint Bernard': [],
        'Samoyed': [],
        'Shih Tzu': [],
        'Siberian Husky': ['Husky'],
        'Weimaraner': [],
        'Whippet': [],
        'Xoloitzcuintli': [
            'Mexican Hairless Dog', 'Hairless Dog',
            'Mexican Hairless',
        ],
    }

    def __init__(self):

        breed_names = []

        for breed, alt_names in self.breeds.items():
            breed_names.append((breed, breed))
            for alt_name in alt_names:
                breed_names.append((breed, alt_name))

        single_hashtags = {
            util.fold_hashtag(name): breed
            for breed, name in breed_names
        }

        plural_hashtags = {
            util.fold_hashtag(name) + 's': breed
            for breed, name in breed_names
        }

        self.breed_hashtags = {**single_hashtags, **plural_hashtags}

    def name_from_hashtag(self, hashtag):
        return self.breed_hashtags.get(hashtag, None)
