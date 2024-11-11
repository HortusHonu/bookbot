def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    result_dict = count_characters(text)
    character_sorted_list = characters_dict_to_sorted_list(result_dict)

    # print(text)
    # print(f"{word_count} words found")
    # print(result_dict)    

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()

    for item in character_sorted_list:
        if not item['character'].isalpha():
             continue
        print(f"The '{item['character']}' character was found {item['num']} times")

    print("--- END REPORT ---")
     

def get_book_text(path):
        with open(path) as f:
            return f.read()

def count_words(text):
     return len(text.split())

def count_characters(text):
    characters = {}

    for letter in text:
        lowered = letter.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1

    return characters

def sort_on(dict_list):
     return dict_list["character"] # Can also set to "num" key

def characters_dict_to_sorted_list(character_dict):
     sorted_list = []
     for char in character_dict:
          sorted_list.append({"character": char, "num": character_dict[char]})
     sorted_list.sort(reverse=True, key=sort_on)
     return sorted_list
     

main()