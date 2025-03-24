from stats import words_count, character_count, dict_sorted
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = get_book_text(sys.argv[1])
    num_words = words_count(book)
    all_characters = character_count(book)
    intro = """============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------"""
    print(intro)
    print(f"Found {num_words} total words\n--------- Character Count -------")
    report = dict_sorted(all_characters)
    for entry in report:
        if  entry["character"].isalpha():
            print(f"{entry['character']}: {entry['count']}")
    print("============= END ===============")
main()
