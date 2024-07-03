import random

def get_numbers_ticket(minimum, maximum, quantity):
    if not (1 <= minimum <= maximum <= 1000):
        return []

    numbers_set = set()

    while len(numbers_set) < quantity:
        random_number = random.randint(minimum, maximum)
        numbers_set.add(random_number)

    sorted_numbers = sorted(numbers_set)
    return sorted_numbers
