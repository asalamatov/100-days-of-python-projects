def number(start_number, end_number):
    """Generates a random number in the given range"""
    import random
    list_of_numbers = []
    for i in range(start_number, end_number+1):
        list_of_numbers.append(i)
    random_number = random.choice(list_of_numbers)
    return random_number