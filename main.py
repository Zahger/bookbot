def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = get_num_words(text)
    print(f"{word_count} words found in the document")
    print(count_character(text))


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import get_num_words

from stats import count_character

main()