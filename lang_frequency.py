import sys
import string


exclude = list(string.punctuation)
exclude.append(chr(8211))


def load_data(file_path):
    dict_words = {}
    with open(file_path, 'r') as file_handler:
        for line in file_handler:
            line = ''.join(i for i in line if i not in exclude).split()
            for word in line:
                word = word.lower()
                dict_words[word] = dict_words.get(word, 0) + 1
    return dict_words


def get_most_frequent_words(dict_words):
    dict_max_value = {}
    for i in range(10):
        key_max_value = (max(dict_words.keys(), key=lambda x: dict_words[x]))
        max_value = dict_words.get(key_max_value)
        dict_max_value.update({key_max_value: max_value})
        dict_words.pop(key_max_value, max_value)
    return dict_max_value


def pprint_most_frequent_words(dict_max_value):
    sorted_by_value = sorted(
        dict_max_value,
        key=lambda x: int(dict_max_value[x]),
        reverse=True
        )
    for key in sorted_by_value:
        print(key, ':', dict_max_value.get(key))


def main():
    try:
        file_path = sys.argv[1]
        dict_max_value = get_most_frequent_words(load_data(file_path))
        pprint_most_frequent_words(dict_max_value)
    except IndexError:
        print(' Error: No filename for reading!\n')
    except FileNotFoundError:
        print(' Error: file or path "{0}" not found!\n'.format(file_path))

if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(' ERROR: {}\n'.format(ex))
