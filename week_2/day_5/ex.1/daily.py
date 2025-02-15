#1
# What is a class?-יצירת מחלקה כל שהיא 
# What is an instance?-
# What is encapsulation?-
# What is abstraction?-
# What is inheritance?-
# What is multiple inheritance?-
# What is polymorphism?-
# What is method resolution order or MRO?-


#2
import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"
class Deck:
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(suit, value) for suit in self.suits for value in self.values]

    def shuffle(self):
        if len(self.cards) == 52:
            random.shuffle(self.cards)
        else:
            print("Cannot shuffle. Some cards have been dealt.")

    def deal(self):
        if len(self.cards) > 0:
            return self.cards.pop(0)
        else:
            return "No more cards left in the deck."

deck = Deck()
deck.shuffle()
print(deck.deal())
print(deck.deal())
print(len(deck.cards))
