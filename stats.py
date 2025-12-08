def get_num_words(s):
    num_words = 0
    words = s.split()
    for word in words:
        num_words += 1
    return num_words


def count_character(test):
    dict_of_chars = {}

    for c in test:
        lowerd = c.lower()
        if lowerd in dict_of_chars:
            dict_of_chars[lowerd] += 1
        else:
            dict_of_chars[lowerd] = 1

    return dict_of_chars


def get_book_text(path):
    with open(path) as f:
        s = f.read()
    return s


def sort_num(items):
    return next(iter(items.values()))


def get_analyse(dicts):
    anal = []

    for ch, num in dicts.items():
        if ch.isalpha():
            anal.append({
                ch: num
            })
    anal.sort(key=sort_num, reverse=True)
    return anal
