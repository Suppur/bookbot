def main():
    path_to_file = "books/frankenstein.txt"
    files_contents = get_book_text(path_to_file)
    words_total = word_counter(files_contents)
    letters_total = letter_counter(files_contents)
    sorted_char_list = sorted_letter_dic_list(letters_total)

    print(f"--- Begin report of {path_to_file} ---")
    print(f"{words_total} words found in the document")
    print()

    for item in sorted_char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")
def word_counter(words_string):
    words = words_string.split()
    return(len(words))

def sort_on(dic):
    return dic["num"]

def sorted_letter_dic_list(letter_dic):
    sorted_list = []
    for c in letter_dic:
        sorted_list.append({"char": c, "num": letter_dic[c]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def letter_counter(words):
    letter_dic = {}
    for word in words:
        lowered_word = word.lower()
        if lowered_word in letter_dic and lowered_word.isalpha():
            letter_dic[lowered_word] += 1
        elif lowered_word.isalpha():
            letter_dic[lowered_word] = 1
    return letter_dic

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
