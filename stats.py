from operator import itemgetter

def get_num_words(path_to_file):
    with open(path_to_file) as f:
        file_contents=f.read()
    return f"Found {len(file_contents.split())} total words"

def get_quantity_characters(path_to_file):
    with open(path_to_file) as f:
        file_contents=f.read()

    quantities = {}

    for letter in file_contents:
        letter = letter.lower()
        if letter not in quantities:
            quantities[letter] = 1
        else:
            quantities[letter] += 1
    
    return quantities

def get_dictionary_characters(path_to_file):
    dictionary = get_quantity_characters(path_to_file)

    list_dictionaries=list()

    for item in dictionary:
        if item not in list_dictionaries:
            if item.isalpha():
                list_dictionaries.append({"char":item,"num":dictionary[item]})

    list_dictionaries = sorted(list_dictionaries, key=itemgetter("num"), reverse=True)

    return list_dictionaries


def sort_on(items):
    return items["num"]