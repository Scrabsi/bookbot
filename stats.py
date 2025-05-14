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

def get_sorted