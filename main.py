def main():
    import sys
    try:
        path_to_file = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(path_to_file)
    word_count = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("-------- Character Count --------")
    chara_dic = count_character(text)
    clean_dict = clean_on(chara_dic)
    sorted_list = sort_on(clean_dict)
    for key in sorted_list:
        char = key["char"]
        num = key["num"]
        print(f"{char}: {num}")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import get_num_words

from stats import count_character

from stats import clean_on

from stats import sort_on
main()