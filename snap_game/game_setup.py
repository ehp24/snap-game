from snap_game.game_system import Player, Snap_Condition

# Helper class/ Utility class - never instanciated but has methods to call
class Game_Setup:
    
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
            
            print(f"\nHi {name}, you are Player {i+1}!")
            print(f"{name}, press key [{play_keys[i]}] to play a card on your pile, and key [{snap_keys[i]}] to call Snap!", end = "\n\n")
            
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
        print(f"[{match_keys['both']}]: matching value AND suit i.e. same card - NOTE: for this option you must select more than one pack of cards to play with.", end='\n\n')
        key_pressed = input(f"Select [{match_keys['suits']}], [{match_keys['value']}] or [{match_keys['both']}]: ")

        while key_pressed not in set(['a','b','c']):
            key_pressed = input(f"Invalid option: please choose either [{match_keys['suits']}], [{match_keys['value']}] or [{match_keys['both']}]: ")

        print(f"\nNice! You chose snap condition [{key_pressed}].", end='\n\n')
        
        return match_keys[key_pressed]

    

    @staticmethod
    def get_decks(snapcondition, max_packs: int):
        try:
            # Require min 2 packs of cards if matching by suit and value i.e. same card
            minpacks = 2 if snapcondition == Snap_Condition.MATCH_SUIT_VALUE else 1

            num_packs = float(input(f"Enter the number of packs of cards to use ({minpacks} to {max_packs}): "))

            if num_packs.is_integer() and minpacks<=int(num_packs) and int(num_packs)<=max_packs :
                num_packs = int(num_packs)
                print(f"\nThanks! {num_packs} pack(s) of cards will be used in the game deck.", end='\n\n')
            else:
                raise ValueError(f"Invalid number: number was not an integer between {minpacks} and {max_packs}.")

        except ValueError:
            print(f"\nInvalid input: please enter an integer value between {minpacks} and {max_packs}.")
            num_packs = Game_Setup.get_decks(snapcondition)
        return num_packs
    
    @staticmethod
    def ready_2_play():
        input("Ready to play? [Press ENTER]:")
        
    @staticmethod
    def get_num_rounds(max_rounds: int):
        try:
            num_rounds = float(input(f"Enter the number of rounds you would like to play (max {max_rounds}): "))
            
            if num_rounds.is_integer() and num_rounds>0 and num_rounds<=max_rounds:
                num_rounds = int(num_rounds)
                print(f"\nGreat, unless a player runs out of cards first, the game will end after {num_rounds} of snap.", end='\n\n')
            else:
                raise ValueError("Invalid number of rounds chosen")
        except ValueError:
            print(f"\nInvalid input: please enter an integer value between 1 and {max_rounds}.")
            num_rounds = Game_Setup.get_num_rounds(max_rounds)
        return num_rounds
        