from stats import count_words
from stats import count_characters
from stats import convert_list
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

def main():
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    
    # Add these two lines inside main():
    character_count = count_characters(text)
    sorted_chars = convert_list(character_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at", sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============") 
    
if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

   

 