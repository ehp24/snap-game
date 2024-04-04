from snap_game.cards import Card, Deck, Player, Game
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
    
def test_deck_draw_card(deck):
    initial_count = len(deck.cards)
    # card_on_top = deck.cards[-1]
    drawn_card = deck.draw()
    assert type(drawn_card) == Card #can use isinstance() to check for subclasses also
    # assert drawn_card == card_on_top 
    assert drawn_card not in deck.cards
    assert len(deck.cards) == initial_count -1
    
    
    
    
@pytest.fixture
def player1():
    return Player("Jane")

def test_player_init(player1):
    assert player1.name == "Jane"
    assert player1.hand == []
    
    

@pytest.fixture
def players():
    return [Player("Jane"),Player("Jack"),Player("Jill")]


def test_game_init(players, deck):
    game = Game(players,deck)
    assert game.players == players
    assert game.game_deck == deck
    
    
@pytest.fixture
def game(players,deck):
    return Game(players,deck)

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
    

    
    
    
    
    
    
    
    