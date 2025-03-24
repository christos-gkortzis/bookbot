def words_count(text):
    list_count = text.split()
    count = len(list_count)
    return count

def character_count(book_text):
    count = dict()
    for char in book_text:
        unique_char = char.lower()
        if unique_char in count:
            count[unique_char] += 1
        else:
            count[unique_char] = 1 
    return count

def dict_sorted(char_dict):
    sorted_characters = []
    for key in char_dict:
        dict_elemant = {"character": key, "count": char_dict[key]}
        sorted_characters.append(dict_elemant)
    def sort_on(dict):
        return dict["count"]
    sorted_characters.sort(reverse=True, key=sort_on)
    return sorted_characters
