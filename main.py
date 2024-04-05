from snap_game.cards import Card, Deck, Player, Game
from snap_game.game_setup import get_players, get_decks

def main():
    print("==============================================")
    print("Welcome to the Game of Snap!", end='\n\n')
    
    # Get list of Player objects using user input
    players = get_players()
    
    # Get number of packs of cards used for game 
    num_packs = get_decks()
    
    # Create game deck
    game_deck = Deck(num_packs)
    
    # Create game object
    game = Game(players,game_deck) 
    
    
    
    
    
    
    
    

    

if __name__ == "__main__":
    main()