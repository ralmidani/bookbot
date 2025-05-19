import sys

from stats import get_num_words, get_character_counts, get_sorted_alpha_counts

def get_book_text(book_filepath):
    with open(book_filepath) as book:
        return book.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")

    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except Exception as e:
        print(f"Book not found at {book_path}")
        sys.exit(1)

    num_words = get_num_words(book_text)
    character_counts = get_character_counts(book_text)
    filtered_and_sorted_counts = get_sorted_alpha_counts(character_counts)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    for count in filtered_and_sorted_counts:
        char = count["char"]
        num = count["num"]
        print(f"{char}: {num}")

main()