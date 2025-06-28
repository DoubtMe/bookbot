import sys
from stats import get_num_words, character_count, sort_dict

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    dict = character_count(text)
    num_words = get_num_words(text)
    print(f"============ BOOKBOT ============\nAnalysing book found at {book_path}\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
    # This doesn't work
    sorted_dict = sort_dict(dict)
    for item in sorted_dict:
       if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
