from .cards import Card, Deck, Pile
import keyboard
import sys
import tty
import termios

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

class Game:
    def __init__(self, players: list[Player], game_deck: Deck) -> None:
        self.players = players
        self.game_deck = game_deck
        self.pile = Pile()
        self.state = "start"
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
        # orginal terminal settings to restore terminal echoing after
        original_terminal_settings = termios.tcgetattr(sys.stdin)
        
        while True:
            self.state="playing"
            
            
            print(f"Please play a card on your pile {self.current_player.name}:")
            tty.setcbreak(sys.stdin.fileno()) # Disable echoing of input characters in console
            keyboard.on_press_key(self.current_player.playkey,self.snap)
            keyboard.wait(self.current_player.playkey)
            
            print(f"Thank you {self.current_player.name}")
            
            self.current_player = self.player2
            print(f"Please play a card on your pile {self.current_player.name}:")
            keyboard.on_press_key(self.current_player.playkey,self.snap)
            keyboard.wait(self.current_player.playkey)
            print(f"Thank you {self.current_player.name}")
            
            print("Game finished")
            # restore terminal settings once game is finished
            termios.tcsetattr(sys.stdin, termios.TCSANOW, original_terminal_settings)
            break
                     
    def snap(self, event):
        print("snapping state invoked")
        print("exiting....snap....")
                    
                    
                                   
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


                    
