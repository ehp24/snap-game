from snap_game.cards import Deck
from snap_game.game_system import Game
from snap_game.game_setup import Game_Setup, End_Condition

def main():
    
    # SET GAME VARIABLES HERE
    max_packs = 5 # max number of packs to use
    max_rounds = 30 # max number of rounds 

    # GAME SETUP:
    Game_Setup.display_intro()
    
    # Get Player objects
    num_players = 2 # fixed for now, have not allowed for multiplayer
    players = Game_Setup.get_players(num_players) 
    
    # Get snap condition
    snap_condition = Game_Setup.get_snap_condition() 
    
    # Get number of packs of cards to use
    num_packs = Game_Setup.get_decks(snap_condition, max_packs) 
    
    # Get end condition and number of rounds
    ending_condition = Game_Setup.get_end_condition() 
    if ending_condition == End_Condition.ROUNDS: 
        num_rounds = Game_Setup.get_num_rounds(max_rounds)
    else: # end condition = until all cards won
        num_rounds = float('inf') # set infinite number of rounds
    
    # Create game object
    game = Game(players, Deck(num_packs), snap_condition, num_rounds) 
    
    print("\n<< Game setup complete >>", end='\n\n')
    game.shuffle_game_deck()
    game.deal_cards()
    input("Ready to play? [Press ENTER]:")
    
    # Game start, will exit this once we have a winner and game is over or ESC pressed
    game.run_game() 
    
    # Game finished
    print("\nThanks for playing!")
    print("===================================================")   

if __name__ == "__main__":
    main()