from stats import book_word_count, count_chars, sort_dict
import sys

def main():
    path_to_book = "books/frankenstein.txt"
    book_contents = get_book_text(path_to_book)

    word_count = book_word_count(book_contents)
    char_count = count_chars(book_contents)
    dict_sort = sort_dict(char_count)

    print("""
============ BOOKBOT ============ \n
Analyzing book found at books/frankenstein.txt...\n
----------- Word Count ----------
""")
    
    print(word_count + "\n")

    print("--------- Character Count -------\n")

    for item in dict_sort:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("\n============= END ===============")

def get_book_text(filepath):
    with open(filepath, 'r', encoding = 'utf-8') as f:
        contents = f.read()
        return contents

main()

""" The solution from boot.dev
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


main()
""" 
