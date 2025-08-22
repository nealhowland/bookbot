import sys
from stats import get_num_words, get_char_count, sort_char_counts


def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as book_file:
        return book_file.read()


def main(book_path):
    book_text = get_book_text(book_path)
    char_counts = get_char_count(book_text)
    sorted_char_counts = sort_char_counts(char_counts)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print(f"--------- Character Count -------")
    for char_count in sorted_char_counts:
        if char_count['char'].isalpha():
            print(f"{char_count['char']}: {char_count['num']}")
    print(f"============= END ===============")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(sys.argv[1])
        sys.exit(0)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
