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

     
def sort_dict(dict):
    new_list = []
    for k, v in dict.items():
        new_list.append({"char": k, "num": v})
    new_list.sort(key=lambda item: item["num"], reverse=True)
    return new_list

