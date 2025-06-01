def get_num_words(text):
        words = text.split()
        return len(words)

def count_character(text):
    chara_count = {}
    lc_words = text.lower()
    for letter in lc_words:
        if letter in chara_count:
            chara_count[letter] += 1
        else:
            chara_count[letter] = 1
    return chara_count