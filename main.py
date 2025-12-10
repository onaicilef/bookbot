from stats import get_book_text, number_of_chars, dictionary_sort
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(get_book_text(sys.argv[1]))
    print("--------- Character Count -------")
    dict = number_of_chars(sys.argv[1])
    sorted_dicts = dictionary_sort(dict)
    for item in sorted_dicts:
        ch = item["char"]
        count = item["num"]
        if ch.isalpha() is True:
            print(f"{ch}: {count}")

    print("============= END ===============")


main()