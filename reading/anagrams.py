import random

def get_word(words_list):
    # Generate letters
    word = random.choice(words_list)
    return word

def anagrams():
    words_list = {'taken': ['an', 'at', 'na', 'eat', 'kat', 'nae', 'tan', 'ant', 'eta', 'net', 'tea', 'ate', 'ten', 'ante', 'kent', 'take', 'tank', 'kane', 'neat', 'teak', 'taken'],
    'rating': ['an', 'at', 'in', 'it', 'na', 'air', 'ant', 'art', 'gin', 'git', 'nag', 'nit', 'rag', 'ran', 'rat', 'rig', 'tag', 'tan', 'tar', 'tin', 'anti', 'gain', 'gait', 'gnat', 'gran', 'grin', 'grit', 'rain', 'rang', 'rant', 'ring', 'tain', 'tang', 'tarn', 'ting', 'trig', 'giant', 'grain', 'grant', 'train', 'rating', 'taring'],
    'steal': ['as', 'at', 'ale', 'alt', 'ate', 'eat', 'est', 'eta', 'let', 'sat', 'sea', 'set', 'tea', 'tel', 'ales', 'alts', 'east', 'eats', 'las', 'lea', 'leas', 'last', 'late', 'lest', 'lets', 'sale', 'salt', 'seal', 'seat', 'slat', 'tale', 'tase', 'teal', 'teas', 'least', 'slate', 'stale', 'steal', 'tales', 'teals', 'tesla'],
    'lease': ['as', 'ale', 'eel', 'sea', 'las', 'see', 'ales', 'ease', 'eels', 'else', 'lase', 'leas', 'lea', 'sale', 'seal', 'easel', 'lease'],
    'tender': ['den', 'end', 'ere', 'net', 'red', 'ret', 'ted', 'tee', 'ten', 'deer', 'deet', 'dent', 'dree', 'need', 'nerd', 'reed', 'rend', 'rent', 'teen', 'tend', 'tree', 'deter', 'ender', 'enter', 'treed', 'trend', 'rented', 'tender']}

    word = get_word(list(words_list.keys()))

    print('Use the letters in the following word to make another word: {}'.format(word))

    guess = input('Enter a word: ')
    if guess in words_list[word]:
        return 'Correct!'
    else:
        return 'Not quite!'

if __name__ == '__main__':
    print(anagrams())



