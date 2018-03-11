import sys
from collections import Counter
import re


def get_most_frequent_words(file_path):
    with open(file_path, 'r') as file_handler:
        all_words = re.findall(r'\w+', file_handler.read().lower())
        most_words = Counter(all_words).most_common(10)
        return most_words


def pprint_words(most_words):
    for i in most_words:
        list(i)
        print(i[0], ':', i[1])


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        most_words = get_most_frequent_words(file_path)
        pprint_words(most_words)
    except IndexError:
        print(' ERROR : No filename for reading!\n')
    except FileNotFoundError:
        print(' ERROR : "{0}" not found or empty!\n'.format(file_path))
