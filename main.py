from snap_game.cards import Card, Deck, Pile
from snap_game.game_system import get_players, get_decks, Game, Player
from snap_game.utils import clear_screen
import time
def main():
    print("==============================================")
    print("Welcome to the Game of Snap!", end='\n\n')
    
    # cut beginning for tetsing purposes
    testing = True
    if testing:
        game= Game([Player("Ellie",'q','z'), Player("Lili",'p','m')],Deck(1))
    else:
        # Get list of Player objects using user input
        players = get_players()
        
        # Get number of packs of cards used for game 
        num_packs = get_decks()
        
        # Create game deck
        game_deck = Deck(num_packs)
        
        # Create game object
        game = Game(players,game_deck) 
    
    # shuffle cards at start fo game:
    print("Shuffling cards...", end='\n\n')
    game.shuffle_game_deck()
    
    # deal cards to players
    print("Dealing cards to players...", end='\n\n')
    game.deal_cards()
    
    game.play()
    
    print("were in mainloop and were done!")
    
    time.sleep(5)

    

if __name__ == "__main__":
    main()