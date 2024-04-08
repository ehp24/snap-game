from snap_game.cards import Card, Deck, Pile
import pytest
from unittest.mock import patch

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
    return Deck(4)

def test_deck_init(deck):
    expected_deck = [str(Card(suit, val)) for _ in range(deck.num_packs) for suit in SUITS for val in RANK]
    test_deck = [str(c) for c in deck.cards]
    assert test_deck == expected_deck
    assert len(deck.cards) == len(expected_deck)
    assert len(deck.cards) == 52*deck.num_packs
    
def test_deck_shuffle(deck):
    original_deck = deck.cards.copy()
    deck.shuffle()
    shuffled_1 = deck.cards.copy()
    assert original_deck != shuffled_1
    deck.shuffle()
    shuffled_2 = deck.cards.copy()
    assert shuffled_2 != shuffled_1

def test_deck_draw_card(deck):
    initial_count = len(deck.cards)
    drawn_card = deck.draw()
    assert type(drawn_card) == Card # can use isinstance() to check for subclasses also
    assert drawn_card not in deck.cards
    assert len(deck.cards) == initial_count -1
    

@pytest.fixture
def pile():
    return Pile()

@pytest.fixture
def pile_with_cards():
    pile_1 = Pile()
    cards = [Card("Diamonds","6"),Card("Clubs","9"),Card("Spades","J")]
    pile_1.cards +=cards
    return pile_1
    
def test_pile_init(pile):
    assert pile.cards == []
    
def test_pile_add_to_pile(pile, card):
    original_pile = pile.cards.copy()
    pile.add_to_pile(card)
    assert len(original_pile) == len(pile.cards) - 1
    assert pile.cards[-1] == card
    
def test_pile_get_top_2_with_empty_pile(pile):
    assert pile.get_top_2() == (None,None)
    
def test_pile_get_top_2_with_single_card_pile(pile, card):
    pile.cards.append(card)
    assert pile.get_top_2() == (None,card)
    
def test_pile_get_top_2(pile_with_cards):
    top_card = pile_with_cards.cards[-1]
    second_card = pile_with_cards.cards[-2]
    assert pile_with_cards.get_top_2() == (second_card, top_card)

def test_pile_clear_all(pile_with_cards):
    pile_with_cards.clear_all()
    assert pile_with_cards.cards == []
    
def test_get_all_cards(pile_with_cards):
    assert pile_with_cards.get_all_cards() == pile_with_cards.cards

