import sys
from stats import get_word_count, get_char_occurrences, sort_by_frequency

def main():
    book_path = ""
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    book = get_book_texts(book_path)
    num_words = get_word_count(book)
    char_occurrences = get_char_occurrences(book)
    sorted_frequencies = sort_by_frequency(char_occurrences)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dic in sorted_frequencies:
        if not dic["char"].isalpha():
            continue
        print(f"{dic["char"]}: {dic["num"]}")
    print("============= END ===============")

def get_book_texts(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
        return file_contents
    
main()