def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_char_count(book_text):
    char_counts = {}
    
    for char in book_text:
        char_counts[char.lower()] = char_counts.get(char.lower(), 0) + 1
    
    return char_counts


def sort_on(items):
    return items["num"]


def sort_char_counts(char_counts):
    unsorted_chars = []

    for char in char_counts:
        count = char_counts[char]
        unsorted_chars.append({'char': char, 'num': count})

    unsorted_chars.sort(reverse=True,key=sort_on)

    return unsorted_chars
