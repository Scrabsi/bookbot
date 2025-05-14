from stats import get_word_count
from stats import get_char_count

def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)
        word_count = get_word_count(text)
        char_count = get_char_count(text)
        print(f"{word_count} words found in the document")
        print(char_count)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



main()