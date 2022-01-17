import sys
import string

def get_next_word(filename):
    try:
        with open(filename, 'r') as reader: 
            for line in reader:
                words = line.split()
                words = [massage_word(word) for word in words if massage_word(word) != '']
                for word in words:
                    yield word
    except FileNotFoundError:
        sys.exit(f"Filename not found: {filename}")        

def massage_word(word):
    trans_table = str.maketrans('','',string.punctuation)
    return word.translate(trans_table)

def create_word_dict(filename):
    words_dict = {}
    for word in get_next_word(filename):
        if words_dict.get(word) is not None:
            words_dict[word] += 1
        else:
            words_dict[word] = 1

    return words_dict

def min_max_word(words_dict):
    min_word = None
    max_word = None

    for word in words_dict.keys():
        if min_word == None or max_word == None:
            min_word = word
            max_word = word
        
        if len(word) < len(min_word):
            min_word = word
        elif len(word) > len(max_word):
            max_word = word

    return min_word, max_word

def get_total_words(words_dict):
    total_words = 0
    for value in words_dict.values():
        total_words += value

    return total_words

def generator_dict_impl(filename):
    words_dict = create_word_dict(filename)
    min_word, max_word = min_max_word(words_dict)
    total_words = get_total_words(words_dict)
    print('Words Dict:' , words_dict)
    print('Unique Words: ', len(words_dict.keys()))
    print('Total Words in Dict: ', total_words)
    print('Min Length word: ', min_word)
    print('Max Length word: ', max_word)


if __name__ == '__main__':
    filename = sys.argv[1]
    generator_dict_impl(filename)
