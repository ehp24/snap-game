from snap_game.game_system import Player, Snap_Condition
from enum import Enum
import time

class End_Condition(Enum):
    ROUNDS = 0
    ALL_CARDS = 1

# Helper class/ Utility class - grouping all game setup functions here
class Game_Setup:
    
    @staticmethod
    def display_intro():
        print("===================================================")
        print("Welcome to the game of Snap!", end='\n\n')
        print("<< Instructions >>")
        print("The aim of the game is to win cards by calling SNAP when the two cards on the top of the pile match by a certain condition.")
        print("If you call snap correctly, the cards in the pile will be added to your hand.")
        print("A round is finished when a player successfully calls snap.")
        print("The player with the most cards in their hand at the end of the game is the winner!", end='\n\n')
        
    @staticmethod
    def get_players(num_players: int):
        players = [None]*num_players
        player_names = set()
        play_keys = ["q","p"] # two keys as only two players for now
        snap_keys = ["z", "m"] # predefined keys for now, can let players choose if extended

        for i in range(0,num_players):
            name = input(f"Enter Player {i+1}'s name: ")
            while name in player_names:
                name = input(f"Sorry, player with that name already exists. Please enter another name: ")
            
            player_names.add(name)
            players[i] = Player(name,play_keys[i], snap_keys[i])
            print(f"Hi {name}, you are Player {i+1}!")
            print(f"{name}, press key [{play_keys[i]}] to play a card on your pile, and key [{snap_keys[i]}] to call Snap!", end = "\n\n")
            time.sleep(4)
            
        return players
    
    @staticmethod
    def get_snap_condition():
        match_keys = {'suits': 'a',
                    'value': 'b',
                    'both': 'c',
                    'a': Snap_Condition.MATCH_SUIT,
                    'b': Snap_Condition.MATCH_VALUE,
                    'c': Snap_Condition.MATCH_SUIT_VALUE}

        print("Choose a condition to call snap for:")
        print(f"[{match_keys['suits']}]: matching suit")
        print(f"[{match_keys['value']}]: matching card value")
        print(f"[{match_keys['both']}]: matching value AND suit i.e. same card - NOTE: for this option you must select more than one pack of cards to play with.")
        key_pressed = input(f"Select [{match_keys['suits']}], [{match_keys['value']}] or [{match_keys['both']}]: ")

        while key_pressed not in set(['a','b','c']):
            key_pressed = input(f"Invalid option: please choose either [{match_keys['suits']}], [{match_keys['value']}] or [{match_keys['both']}]: ")

        print(f"Nice! You chose snap condition [{key_pressed}].", end='\n\n')
        time.sleep(2)
        return match_keys[key_pressed]

    @staticmethod
    def get_decks(snapcondition, max_packs: int):
        try:
            minpacks = 2 if snapcondition == Snap_Condition.MATCH_SUIT_VALUE else 1 # can only match by suit + value if > 1pack
            num_packs = float(input(f"Enter the number of packs of cards to use ({minpacks} to {max_packs}): "))
            if num_packs.is_integer() and minpacks<=int(num_packs) and int(num_packs)<=max_packs :
                num_packs = int(num_packs)
                print(f"Thanks! {num_packs} pack(s) of cards will be used in the game deck.", end='\n\n')
                time.sleep(2)
            else:
                raise ValueError(f"Invalid input recieved")
        except ValueError:
            print(f"Invalid input: please enter an integer value between {minpacks} and {max_packs}.")
            num_packs = Game_Setup.get_decks(snapcondition, max_packs)
        return num_packs
    
    @staticmethod
    def get_num_rounds(max_rounds: int):
        try:
            num_rounds = float(input(f"Enter the number of rounds you would like to play (max {max_rounds}): "))
            if num_rounds.is_integer() and num_rounds>0 and num_rounds<=max_rounds:
                num_rounds = int(num_rounds)
                print(f"Great, unless a player runs out of cards first, the game will end after {num_rounds} rounds of snap.", end='\n\n')
                time.sleep(4)
            else:
                raise ValueError("Invalid number of rounds chosen")
        except ValueError:
            print(f"Invalid input: please enter an integer value between 1 and {max_rounds}.")
            num_rounds = Game_Setup.get_num_rounds(max_rounds)
        return num_rounds
    
    @staticmethod
    def get_end_condition():
        conditions = {'a': End_Condition.ROUNDS,
                      'b': End_Condition.ALL_CARDS}
        
        print("Choose a condition for game end:")
        print("[a]: after X number of rounds")
        print("[b]: until a player has won all the cards in the game")
        end_condition = input(f"Select [a] or [b]: ")
        while end_condition not in set(['a','b']):
            end_condition = input(f"Invalid option: please choose either [a] or [b]: ")
            
        print(f"Thanks! You chose end condition [{end_condition}].", end='\n\n')
        time.sleep(1)
        return conditions[end_condition]
            
            
            
            
            
 
        
        