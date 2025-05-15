from stats import get_word_count, get_char_count, get_sorted

def main():
        book_path = "books/frankenstein.txt"
        text = get_book_text(book_path)    #is string
        word_count = get_word_count(text)  #is int
        char_count = get_char_count(text)  #is dictionary
        sorted_dict = get_sorted(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for item in sorted_dict:
             if item["char"].isalpha():
                  print(f"{item["char"]}: {item["num"]}")
        print("============= END ===============")
def get_book_text(path_to_file):
    with open(path_to_file, encoding="utf8") as f:
        file_contents = f.read()
    return file_contents



main()