def count_chars(text):
    letters = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVWYXZ"
    numbers = "0123456789"

    counts = {
        'letters': 0,
        'numbers': 0,
        'space': 0,
        'other': 0,
    }

    for char in text:

        if char in letters:
            counts['letters'] += 1

        if char in numbers:
            counts['numbers'] += 1

        if char == ' ':
            counts['space'] += 1

        else:
            counts['other'] += 1

    return counts