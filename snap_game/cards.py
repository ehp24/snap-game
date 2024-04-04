import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    
    def get_suit(self):
        return self.suit
    
    def get_value(self):
        return self.value
    
    def __str__(self) -> str:
        return f"{self.value} {self.suit}"
        
SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
RANK = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]


class Deck:
    def __init__(self) -> None:
        self.cards = [Card(suit, val) for suit in SUITS for val in RANK]
        
    def shuffle(self):
        return random.shuffle(self.cards)
    
    def get_cards(self):
        for card in self.cards:
            print(card)
        
        




    
