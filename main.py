def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count -----------")
    print(f"{word_count} words found in the document")
    print("-------- Character Count --------")
    chara_dic = count_character(text)
    clean_dict = clean_on(chara_dic)
    sort_on(clean_dict)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

from stats import get_num_words

from stats import count_character

from stats import clean_on

main()