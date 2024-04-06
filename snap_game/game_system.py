from .cards import Card, Deck, Pile
import sys
import tty
import termios
from pynput import keyboard
from enum import Enum


        
# orginal terminal settings to restore terminal echoing after
ORIGINAL_TERMINAL_SETTINGS = termios.tcgetattr(sys.stdin)
# from pynput import keyboard

class Player:
    def __init__(self, name: str, playkey: str, snapkey:str) -> None:
        self.name = name
        self.hand = [] # players always start with empty hands
        self.playkey = playkey
        self.snapkey = snapkey
    
    def play_card(self):
        try:
            return self.hand.pop() # card played is last card in hand list
        
        except IndexError:
            print("Cannot play card as hand is empty")
            return None
    
    def show_hand(self):
        cards_in_hand = [str(card) for card in self.hand]
        return cards_in_hand
        

class Game_State(Enum):
    SETUP = 0
    PLAY = 1
    SNAP = 2
    END = 3
        
    
    
class Game:
    def __init__(self, players: list[Player], game_deck: Deck) -> None:
        self.players = players
        self.game_deck = game_deck
        self.pile = Pile()
        self.state = Game_State.PLAY
        self.player1 = self.players[0]
        self.player2 = self.players[1]
        self.current_player = self.player1

        

    def shuffle_game_deck(self):
        self.game_deck.shuffle()
        
    def deal_cards(self):
        # draw cards one by one and append to each Player's hand until deck is empty
        while self.game_deck.cards:
            for player in self.players:
                if self.game_deck.cards:
                    drawn_card = self.game_deck.draw()
                    player.hand.append(drawn_card) 
                    
    def play(self):

        
        while self.state == Game_State.PLAY:
            

            tty.setcbreak(sys.stdin.fileno()) # Disable echoing of input characters in console
            print(f"{self.current_player.name}, play a card on the pile by pressing your play key [{self.current_player.playkey}]:")
            
            
            with keyboard.Listener(on_press=self.on_press) as listener:
                listener.join()

            
                
        
    def card_played(self):

        print("Inside card played fucntion!")
        played_card = self.current_player.play_card()
        
        if not played_card: # if play_card() returns none:
            print(f"Card could not be placed as {self.current_player.name}'s hand is empty. Ending game")
            self.game_end()
        else:
        # only one pile in whole game so dont need to pass pile into card_played
            self.pile.add_to_pile(played_card)
            print("You played a",played_card)
            (card1, card2) = self.pile.get_top_2()
            print(f"Cards at top of pile: {card1.show_card() if card1 else 'empty pile'} , {card2.show_card() if card2 else ('empty pile')}", end='\n\n' )
            self.switch_current_player()
            



    def on_press(self, key):
        
        try:
            if key.char in [player.playkey for player in self.players]:
                # KEEP GAME STATE
                self.card_played()
            elif key.char in [player.snapkey for player in self.players]:
                # CHANGE GAME STATE TO SNAP PHASE
                self.snap()
            else:
                print(f"You pressed an invalid key. Please press [{self.current_player.playkey}] to play a card on the pile or [{self.current_player.snapkey}] to call snap")
            return False
                
        except AttributeError:
            print(f"You pressed an invalid key. Please press [{self.current_player.playkey}] to play a card on the pile or [{self.current_player.snapkey}] to call snap")



    def game_end(self):
        print("Game ending")
        
        print(f"cards in pile [{len(self.pile.show_all_cards())} in total]:")
        print(f"{self.pile.show_all_cards()}")
        
        
        print(f"cards in {self.player1.name}'s hand [{len(self.player1.show_hand())} in total]: ")
        print(f"{self.player1.show_hand()}")

        print(f"cards in {self.player2.name}'s hand [{len(self.player2.show_hand())} in total]: ")
        print(f"{self.player2.show_hand()}")
        
        print("exitting game end...")
        
        # restore terminal settings once game is finished
        termios.tcsetattr(sys.stdin, termios.TCSANOW, ORIGINAL_TERMINAL_SETTINGS)
        
        self.state = Game_State.END
                     
    def snap(self, event):
        self.state = Game_State.SNAP
        print("snapping state invoked")
        print("exiting....snap....")
        self.game_end()
        
        
    def switch_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        
        
        
        
                    
                    
                                   
def get_players():
    num_players = 2 # fix for now 
    
    players = [None]*num_players
    player_names = set()
    play_keys = ["q","p"] # two keys as only two players for now
    snap_keys = ["z", "m"]
    
    for i in range(0,num_players):
        name = input(f"Enter Player{i+1}'s name: ")
        while name in player_names:
            name = input(f"Sorry, player with that name already exists. Please enter another name Player{i+1}: ")
        
        player_names.add(name)
        print(f"Hi {name}, you are Player{i+1}!" , end='\n\n')
        print(f"{name}, please press key: {play_keys[i]} , to play a card on your pile, and key: {snap_keys[i]} , to call Snap! ")
        # playkey = input(f"{name}, please choose a key for playing a card on your pile, it must be a single lower case character: ")
        
        # while not check_valid_key(playkey):
        
        players[i] = Player(name,play_keys[i], snap_keys[i])
        
    return players

# def check_valid_key(key):
#     if len(key) == 1 and ord(key)>=97 and ord(key)<=122:
#         return True
#     else:
#         return False
    
    

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


                    
