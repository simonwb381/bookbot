def number_of_words(a):
    words = a.split()
    return len(words)


def number_each_character(book_text):
    low_case = book_text.lower()
    counts = {}
    for ch in low_case:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    #print(counts)
    return counts


def sort_list(dictionary):
    list_dictionaries = []
    for ch in dictionary:
        entry = {"char" : ch, "num" : dictionary[ch]}
        list_dictionaries.append(entry)
    list_dictionaries.sort(reverse=True, key=return_num)
    return list_dictionaries

def return_num(dict):
    return dict["num"]

