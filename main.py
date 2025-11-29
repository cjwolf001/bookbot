from stats import get_num_words, get_quantity_characters,get_dictionary_characters
import sys
print("Usage: python3 main.py <path_to_book>")


def main():

    path_to_file = sys.argv[1]

    words=get_num_words(path_to_file)

    list_dictionary = get_dictionary_characters(path_to_file)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in list_dictionary:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
main()
