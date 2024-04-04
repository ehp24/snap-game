from snap_game.cards import Card, Deck, Player, Game
from snap_game.game_setup import get_players
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
    
    
