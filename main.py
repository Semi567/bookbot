def main():
    with open(book) as f:
        file_contents = f.read()
    print(file_contents)

def count_words(text):
    with open(text) as f:
        file_contents = f.read()
    words = file_contents.split()   
    return len(words)

def count_characters(text):
    with open(text) as f:
        file_contents = f.read()
    lowered_char_text = file_contents.lower()
    char_amount = {}
    for c in lowered_char_text:
        if c in char_amount:
            char_amount[c] += 1
        else:
            char_amount[c] = 1
    return char_amount

def sort_on(dict):
    return dict["num"]

def list_of_dicts(dict):
    lst = []
    
    for k in dict:
        if k.isalpha():
            dict_tmp = {"letter": k, "num": dict[k]}
            lst.append(dict_tmp)
    return lst

def decorated_letters(list):
    for i in range(len(list)):
        print(f"The letter \'{list[i]["letter"]}\' appeared {list[i]["num"]} times.")


book = "books/frankenstein.txt"

#main()
print("--- Begin report of books/frankenstein.txt ---")
print(f"{count_words(book)} - amount of words in the book")
print()
dictionary_1 = count_characters(book)
list_1 = list_of_dicts(dictionary_1)
list_1.sort(reverse=True, key=sort_on)
decorated_letters(list_1)
print("--- End report ---")
