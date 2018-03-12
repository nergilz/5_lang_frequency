import sys
import re
import os
from collections import Counter


def load_data(file_path):
    with open(file_path, 'r') as file_handler:
        all_words = re.findall(r'\w+', file_handler.read().lower())
        return all_words


def get_most_frequent_words(all_words, encountered_words):
    most_frequent_words = Counter(all_words).most_common(encountered_words)
    return most_frequent_words


def file_is_empty(file_path):
    return os.stat(file_path).st_size == 0


def pprint_words(most_frequent_words):
    for word, count in most_frequent_words:
        print(word, ':', count)


def main(file_path, encountered_words):
    if file_is_empty(file_path):
        print(' ERROR: This file "{}" is empty!\n'.format(file_path))
    else:
        try:
            all_words = load_data(file_path)
            most_frequent_words = get_most_frequent_words(all_words, encountered_words)
            pprint_words(most_frequent_words)
        except UnicodeDecodeError:
            print(' ERROR: decode error, file must be .txt!\n')


if __name__ == '__main__':
    try:
        file_path = sys.argv[1]
        encountered_words = int(sys.argv[2])
        main(file_path, encountered_words)
    except FileNotFoundError:
        print(' ERROR: file "{}" not found!\n'.format(file_path))
    except IndexError:
        print(' ERROR: No filename for reading and must be two argument!\n')
    except ValueError:
        print(' ERROR: encountered words argument must be int()\n')
