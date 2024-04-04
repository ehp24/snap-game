# file containing functions for setting up and initiating the snap game
from .cards import Card, Deck, Player, Game

def get_players():
    num_players = 2 # fix for now 
    
    players = [None]*num_players
    player_names = set()
    
    for i in range(0,num_players):
        name = input(f"Enter Player{i+1}'s name: ")
        while name in player_names:
            name = input(f"Sorry, player with that name already exists. Please enter another name Player{i+1}: ")
        
        player_names.add(name)
        print(f"Hi {name}, you are Player{i+1}!" , end='\n\n')
        players[i] = Player(name)
        
    return players