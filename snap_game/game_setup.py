from snap_game.game_system import Player, Snap_Condition

# Helper class/ Utility class - never instanciated but has methods to call
class Game_Setup:
    @staticmethod
    def get_snap_condition():
        match_keys = {'suits': 'a',
                    'value': 'b',
                    'both': 'c',
                    'a': Snap_Condition.MATCH_SUIT,
                    'b': Snap_Condition.MATCH_VALUE,
                    'c': Snap_Condition.MATCH_SUIT_VALUE}

        print("Choose a condition to call snap for:")
        print(f"[{match_keys['suits']}]: matching suit e.g. Spade and Spade")
        print(f"[{match_keys['value']}]: matching card value e.g. A and A")
        print(f"[{match_keys['both']}]: matching value AND suit e.g. A Spades and A Spades. If you choose this, you must choose more than one pack of cards to play with.")
        key_pressed = input(f"Select [{match_keys['suits']}], [{match_keys['value']}] or [{match_keys['both']}]: ")

        while key_pressed not in set(['a','b','c']):
            key_pressed = input(f"Invalid option: please choose either [{match_keys['suits']}], [{match_keys['value']}] or [{match_keys['both']}]: ")

        print(f"Nice! The snap condition will be {[key_pressed]}.")
        return match_keys[key_pressed]

    @staticmethod
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

    @staticmethod
    def get_decks(snapcondition):
        try:
            if snapcondition == Snap_Condition.MATCH_SUIT_VALUE:
                minpacks = 2
            else:
                minpacks = 1
            num_packs = float(input(f"Enter the number of packs of cards to use ({minpacks} to 5): "))
            print(" ")
            if num_packs.is_integer() and minpacks<=int(num_packs) and int(num_packs)<=5 :
                num_packs = int(num_packs)
                print(f"{num_packs} packs of cards will be used in the game deck.", end='\n\n')
            else:
                raise ValueError(f"Invalid number: number was not an integer between {minpacks} and 5.")

        except ValueError:
            print(f"Invalid input: please enter an integer value between {minpacks} and 5.")
            num_packs = Game_Setup.get_decks(snapcondition)
        return num_packs