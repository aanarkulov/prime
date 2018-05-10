import random, string, re
from django.utils.text import slugify

from slugify import slugify, Slugify, UniqueSlugify
base_slugify = Slugify(to_lower=True)

# Generate random strings for slugifier
def random_string_generator(size=15, chars=string.ascii_lowercase + string.ascii_uppercase + string.hexdigits):
    return ''.join(random.choice(chars) for _ in range(size))