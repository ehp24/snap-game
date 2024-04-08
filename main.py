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
    print("===================================================")
    print("Welcome to the game of Snap!", end='\n\n')
    print("<< Instructions >>")
    print("The aim of the game is to win cards by calling SNAP when the two cards on the top of the pile match by a certain condition.")
    print("If you call snap correctly, the cards in the pile will be added to your hand.")
    print("A round is finished when a player successfully calls snap.")
    print("The player with the most cards in their hand at the end of the rounds is the winner!", end='\n\n')

    
    # cut beginning for tetsing purposes
    testing = 0
    if testing:
        game= Game([Player("Ellie",'q','z'), Player("Lili",'p','m')],Deck(1),Snap_Condition.MATCH_VALUE,num_rounds)
    else:
        # Game setup:
        
        # Number of players, 2 by defualt, if not create fucntion to collect user input for this
        num_players = 2 # fix for now 
        
        # Get list of Player objects using user input
        players = Game_Setup.get_players(num_players)
        
        # Get matching condition
        snap_condition = Game_Setup.get_snap_condition()
        
        # Get number of packs of cards used for game 
        max_packs = 5 # set the maximum number of packs to use here
        num_packs = Game_Setup.get_decks(snap_condition, max_packs)
        
        # Get number of rounds to play
        max_rounds = 30 # set maximum number of rounds here
        num_rounds = Game_Setup.get_num_rounds(max_rounds)
        
        # Create game deck
        game_deck = Deck(num_packs)
        
        # Create game object
        game = Game(players,game_deck,snap_condition,num_rounds) 
    
    print("\n<< Game setup complete >>", end='\n\n')
    # shuffle cards at start of game:
    print("Shuffling cards...", end='\n\n')
    game.shuffle_game_deck()
    
    # deal cards to players
    print("Dealing cards to players...", end='\n\n')
    game.deal_cards()
    
    Game_Setup.ready_2_play()
    
    game.run_game() # Game started, will exit this once we have a winner and game is over

    print("\nThanks for playing!")
    print("===================================================")
    sys.stdin.flush()
    

    

if __name__ == "__main__":
    main()