from anagram_checker import AnagramChecker


def main():
    checker = AnagramChecker(r'C:\Users\Rony\Desktop\di_bootcamp\week_2\day_5\ex.1\words.txt')

    while True:
        print("\nMenu:")
        print("1. Input a word")
        print("2. Exit")
        choice = input("Choose an option (1/2): ")

        if choice == '2':
            print("Exiting program. Goodbye!")
            break

        elif choice == '1':
            word = input("Enter a word: ").strip()

            if " " in word:
                print("Error: Only a single word is allowed.")
                continue

            if not word.isalpha():
                print("Error: Only alphabetic characters are allowed.")
                continue

            if checker.is_valid_word(word):
                anagrams = checker.get_anagrams(word)
                print(f"\nYOUR WORD: \"{word.upper()}\"")
                print("This is a valid English word.")
                print(f"Anagrams for your word: {', '.join(anagrams) if anagrams else 'None found'}")
            else:
                print(f"\nThe word \"{word}\" is not valid.")

        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
