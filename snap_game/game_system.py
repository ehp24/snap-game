from .cards import Card, Deck, Pile
from pynput import keyboard
from enum import Enum

class Game_State(Enum):
    PLAY = 0
    SNAP = 1
    WINNER = 2
    END = 3
        
        
class Snap_Condition(Enum):
    MATCH_SUIT = 0
    MATCH_VALUE = 1
    MATCH_SUIT_VALUE = 2
    
    
class Player:
    def __init__(self, name: str, playkey: str, snapkey:str) -> None:
        self.name = name
        self.hand = [] 
        self.playkey = playkey
        self.snapkey = snapkey
    
    def play_card(self):
        try:
            return self.hand.pop() # card played is last card in hand list
        except IndexError: # cannot play card as hand is empty
            return None
    
    def get_hand(self):
        return self.hand
    
    def add_cards_to_hand(self, cardstack = list[Card]):
        cardstack += self.hand
        self.hand = cardstack # add cards to bottmom of hand i.e. begining of list
    
    
class Game:
    def __init__(self, players: list[Player], game_deck: Deck, snap_condition:Snap_Condition, num_rounds) -> None:
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
        self.rounds = num_rounds
        self.round_count = 0
        
    def shuffle_game_deck(self):
        print("Shuffling cards...")
        self.game_deck.shuffle()
        
    def deal_cards(self):
        # draw cards one by one and append to each Player's hand until deck is empty
        print("Dealing cards to players...")
        while self.game_deck.cards:
            for player in self.players:
                if self.game_deck.cards:
                    drawn_card = self.game_deck.draw()
                    player.hand.append(drawn_card) 
                           
    def run_game(self):
        print("\n\n<< Game start >>")
        print("\n*** Press ESC if you want to exit the game at any time ***")
        print("[ROUND 1]")
        
        while self.state != Game_State.END: # when state = end, exit and back to main.py
            if self.state == Game_State.PLAY:
                self.play()
            elif self.state == Game_State.SNAP:
                self.snap()
            elif self.state == Game_State.WINNER:
                self.win()
           
    def play(self):
        print(f"\n{self.current_player.name}, play a card on the pile by pressing your play key [{self.current_player.playkey}]:")
        
        # Start Keyboard Listener for playkeys or snapkeys or ESC
        with keyboard.Listener(on_press=self.on_press,suppress=True) as listener:
            listener.join()
            
    def on_press(self, key):
        
        try:
            if key.char == self.current_player.playkey: 
                self.card_played()
                return False # terminates listener
            elif key.char in [player.snapkey for player in self.players]:
                self.snap_key_pressed = key.char
                self.state = Game_State.SNAP
                return False # terminates listener
            else:
                print(f"You pressed an invalid key. Please press [{self.current_player.playkey}] to play a card on the pile or [{self.current_player.snapkey}] to call snap")
        
        except AttributeError: # keys without char attribute
            
            # Specific script termination key, as SUPRESS=TRUE means normal keyboard terminal functions blocked
            if key == keyboard.Key.esc: 
                print("ESC key pressed")
                self.state = Game_State.END
                return False
            else:
                print(f"You pressed an invalid key! Please press [{self.current_player.playkey}] to play a card on the pile or [{self.current_player.snapkey}] to call snap")
    
    def card_played(self):
        played_card = self.current_player.play_card()
        if not played_card: 
            print(f"Card can not be played as {self.current_player.name}'s hand is empty.", end='\n\n')
            self.state = Game_State.WINNER
        else: 
            self.pile.add_to_pile(played_card)
            print(f"{self.current_player.name}, you played a {played_card}.")
            (card1, card2) = self.pile.get_top_2()
            print(f"Two cards at top of pile:")
            print("-----------------------")
            print(f"{str(card1) if card1 else '(No card)'} | {str(card2) if card2 else '(No card)'}")
            print("-----------------------", end='\n\n')
            self.switch_current_player()
            
    def switch_current_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1   
                            
    def snap(self):
        (card1, card2) = self.pile.get_top_2()
        if card1 == None or card2 == None: # maybe try except this with attribute error i.e. card.suit will error if none
            print("Snap was called incorrectly, please carry on playing.", end='\n\n')
            self.state = Game_State.PLAY
            self.snap_key_pressed = None
            return         
        
        # If snap called correctly:
        if ((self.snap_condition == Snap_Condition.MATCH_SUIT and card1.suit == card2.suit) or
            (self.snap_condition == Snap_Condition.MATCH_VALUE and card1.value == card2.value) or 
            (self.snap_condition == Snap_Condition.MATCH_SUIT_VALUE and card1.value == card2.value and card1.suit == card2.suit)
            ):
            
            # who called snap
            snap_caller = self.player1 if self.snap_key_pressed==self.player1.snapkey else self.player2
            
            # Add pile to caller's hand
            print(f"\nWell done {snap_caller.name}! You correctly called snap, the pile will be added to your hand.", end='\n\n')
            pile_cards = self.pile.get_all_cards()
            snap_caller.add_cards_to_hand(pile_cards)
            self.pile.clear_all() # clear pile
            
            # Update Round and Game State
            self.round_count +=1
            if self.round_count >= self.rounds: 
                self.state = Game_State.WINNER
            else:
                self.state = Game_State.PLAY
                print(f"Number of cards in each player's hand:")
                print(f"{self.player1.name} [{len(self.player1.hand)}], {self.player2.name} [{len(self.player2.hand)}]")
                print(f"\n\n[ROUND {self.round_count+1}]")
                
        else:
            print("Snap was called incorrectly, please carry on playing.")
            self.state = Game_State.PLAY
            self.snap_key_pressed = None
            
        
    def win(self):
        player1_numcards = len(self.player1.get_hand())
        player2_numcards = len(self.player2.get_hand())

        print("\n<< Game Finished >>")
        print(f"{self.player1.name} ends with {player1_numcards} cards, {self.player2.name} ends with {player2_numcards}.", end='\n\n')
        
        print("\n<< Game Result >>")
        if player2_numcards == player1_numcards: 
            print(f"Both players have ended with the same number of cards, it's a Tie!")
        else:
            self.winner = self.player1 if (player1_numcards > player2_numcards) else self.player2
            print(f"Congratulations {self.winner.name}, you won the most cards so you are the winner!")  
        
        self.state = Game_State.END
        