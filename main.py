from snap_game.cards import Card, Deck, Player, Game
from snap_game.game_setup import get_players, get_decks
from pynput import keyboard

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
    
    
    
    
    def on_press(key):
        key_list = ['q','p']
        k = key.char
        if k in key_list:
            print(f"Key pressed: {k}")
    
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    name = input("HI:")

    

# def on_press(key):
#     if key == keyboard.Key.esc:
#         return False  # stop listener
#     try:
#         k = key.char  # single-char keys
#     except:
#         k = key.name  # other keys
#     if k in ['1', '2', 'left', 'right']:  # keys of interest
#         # self.keys.append(k)  # store it in global-like variable
#         print('Key pressed: ' + k)
#         return False  # stop listener; remove this if want more keys

# listener = keyboard.Listener(on_press=on_press)
# listener.start()  # start to listen on a separate thread
# listener.join()  # remove if main thread is polling self.keys
    
    
    

    

if __name__ == "__main__":
    main()