import random

WORDLIST = 'wordlist.txt'

def get_random_word(min_word_length):
    num_words_processed = []
    curr_word = None
    with open(WORDLIST) as f:
        for word in f:
            if '(' or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) < min_word_length:
                continue
            num_words_processed += 1
            if random.randint(1, num_words_processed) == 1:
                curr_word = word
    return curr_word