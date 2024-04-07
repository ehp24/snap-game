from snap_game.cards import Card, Deck, Pile
from snap_game.game_system import Game, Player, Snap_Condition
from snap_game.utils import clear_screen
from snap_game.game_setup import Game_Setup
import time
import sys
import termios
import os
import tty

def main():
    print("==============================================")
    print("Welcome to the Game of Snap!", end='\n\n')
    
    # cut beginning for tetsing purposes
    testing = 0
    if testing:
        game= Game([Player("Ellie",'q','z'), Player("Lili",'p','m')],Deck(1),Snap_Condition.MATCH_VALUE)
    else:
        # Get list of Player objects using user input
        players = Game_Setup.get_players()
        
        # Get matching condiiton
        snap_condition = Game_Setup.get_snap_condition()
        
        # Get number of packs of cards used for game 
        num_packs = Game_Setup.get_decks(snap_condition)
        
        
        # Create game deck
        game_deck = Deck(num_packs)
        
        # Create game object
        game = Game(players,game_deck,snap_condition) 
    
    # shuffle cards at start fo game:
    print("Shuffling cards...", end='\n\n')
    game.shuffle_game_deck()
    
    # deal cards to players
    print("Dealing cards to players...", end='\n\n')
    game.deal_cards()
    
    game.run_game()

     
    
    print("were in mainloop and were done!")
    sys.stdin.flush()
    

    

if __name__ == "__main__":
    main()