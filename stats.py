def get_book_text(path_to_file):
    with open(path_to_file) as f:
        counter = 0
        file_contents = f.read()
        word_count = file_contents.split()
        for word in word_count:
            counter += 1
        result = f"Found {counter} total words"
    return result


def number_of_chars(path_to_file):
    with open(path_to_file) as f:
        letters = {}
        file_contents = f.read()
        for letter in file_contents:
            letter = letter.lower()
            if letter not in letters:
                letters[letter] = 1
            else:
                letters[letter] += 1
    return letters

def dictionary_sort(dict):
    dictionary_list = []
    for d in dict:
        new_dict = {"char": d, "num": dict[d]}
        dictionary_list.append(new_dict)
    def sort_on(items):
        return items["num"]
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list