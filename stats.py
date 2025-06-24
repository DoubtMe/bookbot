characters = {}

def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    for letter in text:
        if letter.lower() in characters:
            characters[letter.lower()] += 1    
        else:
            characters[letter.lower()] = 1
    return characters

# This is where you left off      
def sort_dict():
    pass

character_count("books/frankenstein.txt")
print(characters)