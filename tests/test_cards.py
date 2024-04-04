from snap_game.cards import Card
import pytest

@pytest.fixture
def card():
    return Card("Diamonds", "8")

def test_Card_getters(card):
    assert card.get_suit() == "Diamonds"
    assert card.get_value() == "8"

def test_card_attributes(card):
    assert card.suit == "Diamonds"
    assert card.value == "8"
    
def test_card_str(card):
    assert str(card) == "8 Diamonds"
    
