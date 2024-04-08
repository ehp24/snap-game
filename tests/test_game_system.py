from snap_game.cards import Card, Deck, Pile
from snap_game.game_system import Game, Player, Game_State, Snap_Condition
import pytest
from unittest.mock import patch





@pytest.fixture
def player1():
    return Player("Jane","q","z")

def test_player_init(player1):
    assert player1.name == "Jane"
    assert player1.hand == []
    assert player1.snapkey == "z"
    assert player1.playkey == "q"
    
    
def test_player_play_card(player1):
    cards = [Card("Diamonds","6"),Card("Clubs","9"),Card("Spades","J")]
    player1.hand += cards 

    while player1.hand:
        assert player1.play_card() == cards.pop()
        
def test_player_play_card_from_empty_hand(player1):
    assert player1.play_card() == None
    
def test_player_show_hand(player1):
    cardshand = [str(c) for c in player1.hand]
    assert cardshand == player1.show_hand()


# Test: Class Game_State


def test_enum_values():
    assert Game_State.PLAY.value == 0
    assert Game_State.SNAP.value == 1
    assert Game_State.WINNER.value == 2
    assert Game_State.END.value == 3

def test_enum_names():
    assert Game_State.PLAY.name == "PLAY"
    assert Game_State.SNAP.name == 'SNAP'
    assert Game_State.WINNER.name == 'WINNER'
    assert Game_State.END.name == 'END'

def test_enum_members():
    assert list(Game_State) == [
        Game_State.PLAY,
        Game_State.SNAP,
        Game_State.WINNER,
        Game_State.END
    ]
    
def test_enum_values_are_unique():
    values = [state.value for state in Game_State]
    assert len(values) == len(set(values))

def test_enum_is_immutable():
    with pytest.raises(AttributeError):
        Game_State.PLAY = 5  # Trying to change the value should raise an error





@pytest.fixture
def players():
    return [Player("Jane","a","b"),Player("Jack","c","d")]

@pytest.fixture
def deck():
    return Deck(4)

# def test_game_init(players, deck):
#     game = Game(players,deck)
#     assert game.players == players
#     assert game.game_deck == deck
    
    
@pytest.fixture
def game(players,deck):
    num_rounds=2
    return Game(players,deck, Snap_Condition.MATCH_VALUE, num_rounds)

def test_game_init(game, players, deck):
    assert game.players == players
    assert game.game_deck == deck
    assert type(game.pile) == Pile
    assert game.pile.cards ==[]
    assert game.state == Game_State.PLAY
    assert game.player1 == players[0]
    assert game.player2 == players[1]
    assert game.current_player == game.player1
    assert game.snap_condition == Snap_Condition.MATCH_VALUE
    
    
def test_game_shuffle_game_deck(game):
    deck_before = game.game_deck.cards.copy()
    game.shuffle_game_deck()
    assert game.game_deck.cards != deck_before
    assert len(game.game_deck.cards) == len(deck_before)

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
    

def test_switch_current_player(game):
    game.current_player == game.player1
    game.switch_current_player()
    assert game.current_player == game.player2
    game.switch_current_player()
    assert game.current_player == game.player1









