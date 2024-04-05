from snap_game.cards import Card, Deck, Player, Pile
from snap_game.game_system import get_players, get_decks, Game
import pytest
from unittest.mock import patch

@pytest.fixture
def players():
    return [Player("Jane"),Player("Jack")]

@pytest.fixture
def deck():
    return Deck(4)

def test_game_init(players, deck):
    game = Game(players,deck)
    assert game.players == players
    assert game.game_deck == deck
    
    
@pytest.fixture
def game(players,deck):
    return Game(players,deck)

def test_game_init(game, players, deck):
    assert game.players == players
    assert game.game_deck == deck
    assert type(game.pile) == Pile
    assert game.pile.cards ==[]
    
    

def test_deal_cards(game):
    total_cards = len(game.game_deck.cards)
    num_players = len(game.players)
    
    # deal cards
    game.deal_cards()
    
    player_hands = [len(p.hand) for p in game.players]
    evenly_cards = total_cards // num_players
    leftover_cards = total_cards % num_players
    test_hands = [evenly_cards]*num_players
    for i in range(leftover_cards):
        test_hands[i]+=1
        
    assert len(game.game_deck.cards) == 0
    assert player_hands == test_hands
    
def test_game_shuffle_game_deck(game):
    deck_before = game.game_deck.cards.copy()
    game.shuffle_game_deck()
    assert game.game_deck.cards != deck_before
    assert len(game.game_deck.cards) == len(deck_before)


def test_get_decks_valid_input(monkeypatch):
    input_vals = ["1", "2", "3", "4", "5", "3.0"]
    expected_output = [1, 2, 3, 4, 5, 3]
    
    def mock_input(prompt):
        return input_vals.pop(0)
    
    monkeypatch.setattr('builtins.input', mock_input)
    
    for op in expected_output:
        result = get_decks()
        assert result == op
        

def test_get_decks_invalid_input(monkeypatch):
    input_list = ["-1", "2.5", "3.990", "49", "0", "6", "5"]
    
    def mock_input(prompt):
        return input_list.pop(0)
    
    monkeypatch.setattr('builtins.input', mock_input)
    
    while input_list:
        valid_op = get_decks() #fucntion will keep runnign until we get valid input
        assert valid_op == 5







def test_get_players(monkeypatch):
    input_names = ["Jane", "Jack"]
    expected_players = [Player(name) for name in input_names]
    
    def mock_input(prompt):
        return input_names.pop(0)
    
    monkeypatch.setattr('builtins.input', mock_input)
    
    players = get_players()
    
    assert len(players) == len(expected_players)
    for i in range(len(players)):
        assert type(players[i]) == Player
        assert players[i].name == expected_players[i].name
        assert players[i].hand == expected_players[i].hand
    
    

