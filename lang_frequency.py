import re
from collections import Counter
import argparse


def load_data(file_path):
    with open(file_path, 'r') as file_handler:
        data_from_file = file_handler.read()
        return data_from_file


def get_most_frequent_words(data_from_file, encountered_words):
    all_words = re.findall(r'\w+', data_from_file.lower())
    most_frequent_words = Counter(all_words).most_common(encountered_words)
    return most_frequent_words


def pprint_words(most_frequent_words):
    for word, count in most_frequent_words:
        print(word, ':', count)


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='most frequent words in text')
        file_path = parser.add_argument(
            'file_path',
            type=str,
            help='path for .txt file',
            )
        encountered_words = parser.add_argument(
            'encountered_words',
            type=int,
            help='count of encountered words in text'
            )
        args = parser.parse_args()
        data_from_file = load_data(args.file_path)
        most_frequent_words = get_most_frequent_words(data_from_file, args.encountered_words)
        pprint_words(most_frequent_words)
    except FileNotFoundError:
        print(' ERROR : file "{}" not found\n'.format(args.file_path))
