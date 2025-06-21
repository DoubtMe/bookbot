def get_num_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    characters = {}
    for letter in text:
        if letter.lower() in characters:
            characters[letter.lower()] += 1
            
        else:
            characters[letter.lower()] = 1
    return characters
        


