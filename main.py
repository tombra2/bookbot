from stats import *
import sys

try:
    if sys.argv[1]:
        path = sys.argv[1]
        s = get_book_text(path)
        i = get_num_words(s)
        c = count_character(s)
        analyses = get_analyse(c)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {i} total words")
        print("--------- Character Count -------")
        for anal in analyses:
            for ch, num in anal.items():
                print(f"{ch}: {num}")
        print("============= END ===============")
except:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
