def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    dict = {}
    for char in text.lower():
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return dict 

def sort_on(items):
    return items["num"]


def convert_list(dict):
    empty = []
    for n, value in dict.items():
        new_dict = {"char": n, "num": value}
        empty.append(new_dict)
    empty.sort(reverse=True, key=sort_on)
    return empty