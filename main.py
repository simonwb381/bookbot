import sys
from stats import number_of_words, number_each_character, sort_list



def main():
    #check if sys.argv list has two entries
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]

    # open and read book
    with open(book_path) as f:
        text = f.read()

    # print(text)
    # upper text
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    # word count
    print(f"Found {number_of_words(text)} total words")
    # more text
    print("--------- Character Count -------")

    # makes a dictionary with how much each character has been mentioned
    dictionary = number_each_character(text)
    #print(dictionary)

    # creates a list of dictionaries, consisting of 'char' and 'num'
    sorted_dictionary = (sort_list(dictionary))
    # print(sorted_dictionary)

    # removes non alphabetical characters
    for entry in sorted_dictionary:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")

main()
