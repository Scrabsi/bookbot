#analysis of various things

def get_word_count(text):
     words = text.split()
     word_count = len(words)
     return word_count

def get_char_count(text):
     char_count = {}
     for char in text:
          char = char.lower()
          count = char_count.get(char, 0)
          char_count[char] = count + 1
     return char_count

def get_sorted(dictionary):
    char_list = []
    for char, count in dictionary.items():
        char_dict = {"char": char, "num": count}
        char_list.append(char_dict)
    char_list.sort(reverse=True, key=lambda dict: dict["num"])
    type_char_list = type(char_list)
    return char_list