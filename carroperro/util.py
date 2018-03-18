"""Helpers to create and recognize hashtags"""	
import re


hashtag_patt = re.compile(r'\B#\w*[a-zA-Z]+\w*')


def find_hashtags(text):
    return [hashtag[1:] for hashtag in hashtag_patt.findall(text)]


def fold_hashtag(hashtag):
    """Remove case and non-alphanumerics from hash tags so that minor
    variants will compare equal"""
    return ''.join([char.lower() for char in hashtag if char.isalnum()])


def name_from_hashtag(hashtag, cars, dogs):
    """Return the full name of a dog or car given the hashtag

    Args:
        hashtag (str): the hashtag, which may be either a dog or car hashtag
        cars (Cars): a Cars instance
        dogs (Dogs): a Dogs instance

    Returns:
        string: the full name of the car or dog whose hashtag was supplied

    Raises:
        ValueError: the supplied hashtag was unmatched in cars or dogs
        """
    car_name = cars.name_from_hashtag(hashtag)
    if car_name:
        return 'car', car_name
    dog_name = dogs.name_from_hashtag(hashtag)
    if dog_name:
        return 'dog', dog_name
    raise ValueError('No name found for hashtag: ' + hashtag)


def two_way_index(items):
    """Build a bi-directional lookup table from item -> id and id -> item
    from a list.

    Note this is not valid if any item is an integer in the range of the
    length of the list - 1, as that key will collide with an assigned
    index.

    Args:
        items (list): a list items to be indexed

    Returns:
        dict: from item -> id and id -> item
    """

    lookup = {}

    for index, item in enumerate(items):
        lookup[index] = item
        lookup[item] = index

    return lookup
