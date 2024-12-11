def main():
    book_name = "frankestein.txt"
    book_path = "books/frankestein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = count_characers(text)
    print(f"--- Begin report of {book_name} ---")
    print(f"{num_words} words found in the document")
    for i,j in char_dict.items():
        print(f"The '",i,f"' character was foud {j} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def count_characers(text):
    dictionary = {}
    for i in text:
        i = i.lower()
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    return dictionary

main()