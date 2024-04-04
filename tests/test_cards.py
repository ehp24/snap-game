from snap_game.cards import Card, Deck, Player
import pytest

SUITS = ["Hearts", "Diamonds", "Spades", "Clubs"]
RANK = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

@pytest.fixture
def card():
    return Card("Diamonds", "8")

def test_Card_getters(card):
    assert card.get_suit() == "Diamonds"
    assert card.get_value() == "8"

def test_card_init(card):
    assert card.suit == "Diamonds"
    assert card.value == "8"
    
def test_card_str(card):
    assert str(card) == "8 Diamonds"
    


@pytest.fixture
def deck():
    return Deck()

def test_deck_init(deck):
    expected_deck = [str(Card(suit, val)) for suit in SUITS for val in RANK]
    test_deck = [str(c) for c in deck.cards]
    assert test_deck == expected_deck
    assert len(deck.cards) == 52
    
def test_deck_shuffle(deck):
    original_deck = deck.cards.copy()
    deck.shuffle()
    shuffled_1 = deck.cards.copy()
    assert original_deck != shuffled_1
    deck.shuffle()
    shuffled_2 = deck.cards.copy()
    assert shuffled_2 != shuffled_1
    
    
@pytest.fixture
def player1():
    return Player("Jane")

def test_player_init(player1):
    assert player1.name == "Jane"