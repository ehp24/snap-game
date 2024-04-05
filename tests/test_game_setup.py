from snap_game.cards import Card, Deck, Player, Game
from snap_game.game_setup import get_players, get_decks
import pytest
from unittest.mock import patch


def test_get_players(monkeypatch):
    input_names = ["Jane", "Jack"]
    expected_players = [Player(name) for name in input_names]
    
    def mock_input(prompt):
        return input_names.pop(0)
    
    monkeypatch.setattr('builtins.input', mock_input)
    
    players = get_players()
    
    assert len(players) == len(expected_players)
    for i in range(len(players)):
        assert players[i].name == expected_players[i].name
        assert players[i].hand == expected_players[i].hand
    
    
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
