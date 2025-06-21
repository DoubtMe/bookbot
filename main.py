from stats import get_num_words, character_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    dict = character_count(text)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    print(dict)
    


def get_book_text(path):
    with open(path) as f:
        return f.read()



main()
