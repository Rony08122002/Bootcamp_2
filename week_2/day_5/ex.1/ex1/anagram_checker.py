class AnagramChecker:
    def __init__(self, word_list_file='word.txt'):
        with open(word_list_file, 'r') as file:
            self.word_list = [line.strip() for line in file]
    def is_valid_word(self, word):
        return word.lower() in [w.lower() for w in self.word_list]
    def is_anagram(self, word1, word2):
        return sorted(word1.lower()) == sorted(word2.lower()) and word1.lower() != word2.lower()

    def get_anagrams(self, word):
        if not self.is_valid_word(word):
            return f"{word} is not a valid word."
        anagrams = [w for w in self.word_list if self.is_anagram(word, w)]
        return anagrams if anagrams else f"No anagrams found for {word}."

if __name__ == "__main__":
    checker = AnagramChecker(r'C:\Users\Rony\Desktop\di_bootcamp\week_2\day_5\ex.1\words.txt')


    word = input("Enter a word to check if it's valid: ").strip()
    if checker.is_valid_word(word):
        print(f"{word} is a valid word!")
        anagrams = checker.get_anagrams(word)
        if isinstance(anagrams, list):
            print(f"Anagrams for '{word}': {', '.join(anagrams)}")
    else:
        print(f"{word} is not a valid word.")
