import re
import argparse
from collections import Counter


def load_data(file_path):
    with open(file_path, 'r') as file_handler:
        text_in_file = file_handler.read()
        return text_in_file


def get_most_frequent_words(data_from_file, encountered_words):
    all_words = re.findall(r'\w+', data_from_file.lower())
    most_frequent_words = Counter(all_words).most_common(encountered_words)
    return most_frequent_words


def pprint_words(most_frequent_words):
    for word, count in most_frequent_words:
        print(word, ':', count)


def get_parser_args():
    parser = argparse.ArgumentParser(description='most frequent words in text')
    parser.add_argument(
        'path',
        help='path for .txt file',
    )
    parser.add_argument(
        'number',
        type=int,
        nargs='?',
        default=10,
        help='count of encountered words in text'
    )
    arguments = parser.parse_args()
    return arguments


if __name__ == '__main__':
    try:
        arguments = get_parser_args()
        file_text = load_data(arguments.path)
        most_frequent_words = get_most_frequent_words(file_text, arguments.number)
        pprint_words(most_frequent_words)
    except FileNotFoundError:
        print(' ERROR : file "{}" not found\n'.format(arguments.path))
