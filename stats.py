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

def clean_on(chara_dic):
    letter_count = []
    for letter in chara_dic:
        if letter.isalpha() == True:
            clean_dict = {}
            clean_dict["char"] = letter
            clean_dict["num"] = chara_dic[letter]
            letter_count.append(clean_dict)
    return letter_count