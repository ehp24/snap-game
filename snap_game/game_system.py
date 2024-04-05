from .cards import Card, Deck, Player, Pile

class Game:
    def __init__(self, players: list[Player], game_deck: Deck) -> None:
        self.players = players
        self.game_deck = game_deck
        self.pile = Pile()
        

    def shuffle_game_deck(self):
        self.game_deck.shuffle()
        
    def deal_cards(self):
        # draw cards one by one and append to each Player's hand until deck is empty
        while self.game_deck.cards:
            for player in self.players:
                if self.game_deck.cards:
                    drawn_card = self.game_deck.draw()
                    player.hand.append(drawn_card) 
                    
def get_players():
    num_players = 2 # fix for now 
    
    players = [None]*num_players
    player_names = set()
    
    for i in range(0,num_players):
        name = input(f"Enter Player{i+1}'s name: ")
        while name in player_names:
            name = input(f"Sorry, player with that name already exists. Please enter another name Player{i+1}: ")
        
        player_names.add(name)
        print(f"Hi {name}, you are Player{i+1}!" , end='\n\n')
        players[i] = Player(name)
        
    return players

def get_decks():
    try:
        num_packs = float(input("Enter the number of packs of cards to use (1 to 5): "))
        print(" ")
        if num_packs.is_integer() and 0<int(num_packs) and int(num_packs)<=5 :
            num_packs = int(num_packs)
            print(f"{num_packs} packs of cards will be used in the game deck.", end='\n\n')
        else:
            raise ValueError("Invalid number: number was not an integer between 1 and 5.")
        
    except ValueError:
        print("Invalid input: please enter an integer value between 1 and 5.")
        num_packs = get_decks()
    return num_packs


                    