import sys
from stats import get_num_words, character_count, sort_dict

def main():
    arguments = len(sys.argv)
    if arguments != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        dict = character_count(text)
        num_words = get_num_words(text)
        print(f"============ BOOKBOT ============\nAnalysing book found at {book_path}\n----------- Word Count ----------\nFound {num_words} total words\n--------- Character Count -------")
        sorted_dict = sort_dict(dict)
        for item in sorted_dict:
            if item['char'].isalpha():
                    print(f"{item['char']}: {item['num']}")
        print("============= END ===============")
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
