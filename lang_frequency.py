import sys
from collections import Counter
import re


ENCOUNTERED_WORDS = 10


def get_most_frequent_words(file_path):
    with open(file_path, 'r') as file_handler:
        all_words = re.findall(r'\w+', file_handler.read().lower())
        most_frequent_words = Counter(all_words).most_common(ENCOUNTERED_WORDS)
        return most_frequent_words


def pprint_words(most_frequent_words):
    for word_and_count in most_frequent_words:
        list(word_and_count)
        print(word_and_count[0], ':', word_and_count[1])


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        most_frequent_words = get_most_frequent_words(file_path)
        pprint_words(most_frequent_words)
    except IndexError:
        print(' ERROR : No filename for reading!\n')
    except FileNotFoundError:
        print(' ERROR : file "{0}" not found or empty!\n'.format(file_path))
