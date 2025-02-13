from collections import Counter

class Text:
    def __init__(self, text):
        self.text = text.lower()

    def word_frequency(self, word):
        words = self.text.split()
        freq = words.count(word.lower())
        return freq if freq > 0 else f"The word '{word}' is not in the text"

    def most_common_word(self):
        words = self.text.split()
        word_counts = Counter(words)
        most_common = word_counts.most_common(1)
        return most_common[0][0] if most_common else "Text is empty"

    def unique_words(self):
        words = self.text.split()
        return list(set(words))

    @classmethod
    def from_file(cls, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                text = file.read()
            return cls(text)
        except FileNotFoundError:
            return "File not found!"

# Testing
text_obj = Text.from_file('the_stranger.txt')

if isinstance(text_obj, Text):
    print(text_obj.word_frequency("good"))
    print(text_obj.most_common_word())
    print(text_obj.unique_words())
else:
    print(text_obj)