def book_word_count(text):

    num_words = len(text.split())
    return f"Found {num_words} total words"

def count_chars(text):
    char_count = {}
    
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_dict(char_count):
    sorted_chars = []
    for char, count in char_count.items():
        char_info = {"char": char, "num": count}
        sorted_chars.append(char_info)
    
    def sort_on(dict):
        return dict["num"]
    
    sorted_chars.sort(reverse=True, key=sort_on)

    return sorted_chars

