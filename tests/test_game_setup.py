from snap_game.game_setup import Game_Setup
from snap_game.game_system import Player


def test_get_players(monkeypatch):
    input_names = ["Jane", "Jack"]
    play_keys = ["q", "p"]
    snap_keys = ["z", "m"]
    expected_players = [Player(name, play_key, snap_key) for name, play_key, snap_key in zip(input_names, play_keys, snap_keys)]

    def mock_input(prompt):
        return input_names.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    players = Game_Setup.get_players()

    assert len(players) == len(expected_players)
    for i in range(len(players)):
        assert type(players[i]) == Player
        assert players[i].name == expected_players[i].name
        assert players[i].hand == expected_players[i].hand
        assert players[i].playkey == expected_players[i].playkey
        assert players[i].snapkey == expected_players[i].snapkey


def test_get_decks_valid_input(monkeypatch):
    input_vals = ["1", "2", "3", "4", "5", "3.0"]
    expected_output = [1, 2, 3, 4, 5, 3]

    def mock_input(prompt):
        return input_vals.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    for op in expected_output:
        result = Game_Setup.get_decks()
        assert result == op


def test_get_decks_invalid_input(monkeypatch):
    input_list = ["-1", "2.5", "3.990", "49", "0", "6", "5"]

    def mock_input(prompt):
        return input_list.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)

    while input_list:
        valid_op = Game_Setup.get_decks() #fucntion will keep runnign until we get valid input
        assert valid_op == 5
