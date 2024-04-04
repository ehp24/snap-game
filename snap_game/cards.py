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
    def __init__(self, num_packs: int) -> None:
        self.cards = [Card(suit, val) for _ in range(num_packs) for suit in SUITS for val in RANK]
        self.num_packs = num_packs
        
    def shuffle(self):
        random.shuffle(self.cards)
    
    def get_cards(self):
        for card in self.cards:
            print(card)
    
    def draw(self):
        return self.cards.pop()
    
    # def combine_decks(self,num_decks):
    #     for i in range(num_decks-1):
    #         newdeck = Deck()
    #         self.cards+=newdeck.cards
        
        
        
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = [] # players always start with empty hands
        
        
class Game:
    def __init__(self, players: list[Player], game_deck: Deck) -> None:
        self.players = players
        self.game_deck = game_deck

    def shuffle_game_deck(self):
        self.game_deck.shuffle()
        
    def deal_cards(self):
        # draw cards one by one and append to each Player's hand until deck is empty
        while self.game_deck.cards:
            for player in self.players:
                if self.game_deck.cards:
                    drawn_card = self.game_deck.draw()
                    player.hand.append(drawn_card) 



# deck = Deck()
# players = [Player("Ellie"),Player("Jane")]
# game = Game(players,deck)
# for p in game.players:
#     print(p.name)
#     print(len(p.hand))
    
# game.deal_cards()
# for p in game.players:
#     print(p.name)
#     print(len(p.hand))



    
