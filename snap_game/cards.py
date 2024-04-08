import random

SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
RANK = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

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
    
    
class Deck:
    def __init__(self, num_packs: int) -> None:
        self.cards = [Card(suit, val) for _ in range(num_packs) for suit in SUITS for val in RANK]
        self.num_packs = num_packs
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop()


class Pile:
    def __init__(self) -> None:
        self.cards = []
        
    def add_to_pile(self, card: Card):
        self.cards.append(card)
    
    def get_top_2(self) -> tuple:
        num_cards = len(self.cards)
        second_card = self.cards[-2] if num_cards>=2 else None
        first_card = self.cards[-1] if num_cards>=1 else None
        return (second_card, first_card)
    
    def get_all_cards(self): # getter for safer access to all pile cards
        return self.cards
    
    def clear_all(self):
        self.cards = []
    
        

        
        








    
