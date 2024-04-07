from .cards import Card, Deck, Pile
import sys
import tty
import termios
from pynput import keyboard
from enum import Enum
from .utils import clear_screen
import os
        
# orginal terminal settings to restore terminal echoing after
# ORIGINAL_TERMINAL_SETTINGS = termios.tcgetattr(sys.stdin)
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
    
    #PYTEST
    def add_cards_to_hand(self, cardstack = list[Card]):
        # add cards to bottmom of hand i.e. begining of list
        cardstack += self.hand
        self.hand = cardstack
        
        

class Game_State(Enum):
    PLAY = 0
    SNAP = 1
    WINNER = 2
    END = 3
        
# NEED PYTEST
class Snap_Condition(Enum):
    MATCH_SUIT = 0
    MATCH_VALUE = 1
    MATCH_SUIT_VALUE = 2
    
    
class Game:
    def __init__(self, players: list[Player], game_deck: Deck, snap_condition:Snap_Condition) -> None:
        self.players = players
        self.game_deck = game_deck
        self.pile = Pile()
        self.state = Game_State.PLAY
        self.player1 = self.players[0]
        self.player2 = self.players[1]
        self.current_player = self.player1
        self.snap_condition = snap_condition
        self.snap_key_pressed = None
        self.winner = None
        
    def shuffle_game_deck(self):
        self.game_deck.shuffle()
        
    def deal_cards(self):
        # draw cards one by one and append to each Player's hand until deck is empty
        while self.game_deck.cards:
            for player in self.players:
                if self.game_deck.cards:
                    drawn_card = self.game_deck.draw()
                    player.hand.append(drawn_card) 
                    
    # pytest this!!!        
    def run_game(self):
        # a fucntion that continouosly monitors the states of the game and runs the respective fucntions depending on the state
        while self.state != Game_State.END:
            if self.state == Game_State.PLAY:
                self.play()
            elif self.state == Game_State.SNAP:
                self.snap()
            elif self.state == Game_State.WINNER:
                self.win()
        self.game_end()
                
    # NEED TO WRITE PYTEST                
    def play(self):
        
        # tty.setcbreak(sys.stdin.fileno()) # Disable echoing of input characters in console
        print(f"{self.current_player.name}, play a card on the pile by pressing your play key [{self.current_player.playkey}]:")
        
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
            
            
            
                
    # NEED TO WRITE PYTEST  
    def card_played(self):

        print("Inside card played fucntion!")
        played_card = self.current_player.play_card()
        
        if not played_card: # if play_card() returns none:
            print(f"Card could not be placed as {self.current_player.name}'s hand is empty. Ending game")
            self.state = Game_State.END

        else:
        # only one pile in whole game so dont need to pass pile into card_played
            self.pile.add_to_pile(played_card)
            print("You played a",played_card)
            (card1, card2) = self.pile.get_top_2()
            print(f"Cards at top of pile: {card1.show_card() if card1 else 'No card'} , {card2.show_card() if card2 else ('empty pile')}", end='\n\n' )
            self.switch_current_player()
            


    # NEED TO WRITE PYTEST  
    def on_press(self, key):
        
        try:
            if key.char == self.current_player.playkey: 
                # KEEP GAME STATE
                self.card_played()
            elif key.char in [player.snapkey for player in self.players]:
                # CHANGE GAME STATE TO SNAP PHASE
                self.snap_key_pressed = key.char
                self.state = Game_State.SNAP
            else:
                print(f"You pressed an invalid key. Please press [{self.current_player.playkey}] to play a card on the pile or [{self.current_player.snapkey}] to call snap")
            return False
                
        except AttributeError:
            print(f"You pressed an invalid key. Please press [{self.current_player.playkey}] to play a card on the pile or [{self.current_player.snapkey}] to call snap")


    # NEED TO WRITE PYTEST  
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
        # os.system('clear')
        # termios.tcsetattr(sys.stdin, termios.TCSANOW, ORIGINAL_TERMINAL_SETTINGS)
        
        
        
    # NEED TO WRITE PYTEST              
    def snap(self):
        
        # check is snap correct or not
        (card1, card2) = self.pile.get_top_2()
        
        if card1 == None or card2 == None:
            print("Snap was called incorrectly, please carry on playing.")
            self.state = Game_State.PLAY
            self.snap_key_pressed = None
            return         
        
        if self.snap_condition == Snap_Condition.MATCH_SUIT and card1.suit == card2.suit:
                self.state = Game_State.WINNER         
        elif self.snap_condition == Snap_Condition.MATCH_VALUE and card1.value == card2.value:
                self.state = Game_State.WINNER
        elif self.snap_condition == Snap_Condition.MATCH_SUIT_VALUE and card1.value == card2.value and card1.suit == card2.suit:
                self.state = Game_State.WINNER
        else:
            print("Snap was called incorrectly, please carry on playing.")
            self.state = Game_State.PLAY
            self.snap_key_pressed = None
            return
        
        # who called snap
        if self.player1.snapkey ==  self.snap_key_pressed:
            self.winner = self.player1
        else:
            self.winner = self.player2
        
    
    def win(self):
        print(f"Well done {self.winner}! You correctly called snap, card pile will be added to your hand.")
        pile_cards = self.pile.get_all_cards()
        self.winner.add_cards_to_hand(pile_cards)
        # clear pile
        self.pile.clear_all()
        
        print(f"Congratulations! {self.winner.name} won the game!")
        
        self.state = Game_State.END
        
        
    def switch_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

        
        

    # self.snap_condition = 
                     

        
        
        
                    
                    
                                   


                    
