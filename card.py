from abc import ABCMeta, abstractmethod
from enum import Enum
import random


class Suit(Enum):
    HEART = "HEART"
    DIAMOND = "DIAMOND"
    CLUB = "CLUB"
    SPADE = "SPADE"

    def __init__(self, str_name: str) -> None:
        self.str_name = str_name


class Number(Enum):
    A = 1, "A"
    N_2 = 2, "2"
    N_3 = 3, "3"
    N_4 = 4, "4"
    N_5 = 5, "5"
    N_6 = 6, "6"
    N_7 = 7, "7"
    N_8 = 8, "8"
    N_9 = 9, "9"
    N_10 = 10, "10"
    J = 11, "J"
    Q = 12, "Q"
    K = 13, "K"

    def __init__(self, num: int, str_name: str) -> None:
        self.num = num
        self.str_name = str_name
        self.index = self.num - 1


class Card(metaclass=ABCMeta):
    @abstractmethod
    def is_joker(self) -> bool:
        pass

    @abstractmethod
    def get_number(self) -> Number:
        pass

    @abstractmethod
    def get_suit(self) -> Suit:
        pass


class _Joker(Card):
    def is_joker(self) -> bool:
        return True
    
    def get_number(self) -> Number:
        raise NotImplementedError("Joker")
    
    def get_suit(self) -> Suit:
        raise NotImplementedError("Joker")
    
    def __str__(self) -> str:
        return "JOKER"
    

class _NumberCard(Card):
    def __init__(self, suit: Suit, number: Number) -> None:
        self.suit = suit
        self.number = number

    def is_joker(self) -> bool:
        return False

    def get_number(self) -> Number:
        return self.number
    
    def get_suit(self) -> Suit:
        return self.suit
    
    def __str__(self) -> str:
        return f"{self.suit.str_name}-{self.number.str_name}"
    
JOKER = _Joker()
HEART_A = _NumberCard(Suit.HEART, Number.A)
HEART_2 = _NumberCard(Suit.HEART, Number.N_2)
HEART_3 = _NumberCard(Suit.HEART, Number.N_3)
HEART_4 = _NumberCard(Suit.HEART, Number.N_4)
HEART_5 = _NumberCard(Suit.HEART, Number.N_5)
HEART_6 = _NumberCard(Suit.HEART, Number.N_6)
HEART_7 = _NumberCard(Suit.HEART, Number.N_7)
HEART_8 = _NumberCard(Suit.HEART, Number.N_8)
HEART_9 = _NumberCard(Suit.HEART, Number.N_9)
HEART_10 = _NumberCard(Suit.HEART, Number.N_10)
HEART_J = _NumberCard(Suit.HEART, Number.J)
HEART_Q = _NumberCard(Suit.HEART, Number.Q)
HEART_K = _NumberCard(Suit.HEART, Number.K)
DIAMOND_A = _NumberCard(Suit.DIAMOND, Number.A)
DIAMOND_2 = _NumberCard(Suit.DIAMOND, Number.N_2)
DIAMOND_3 = _NumberCard(Suit.DIAMOND, Number.N_3)
DIAMOND_4 = _NumberCard(Suit.DIAMOND, Number.N_4)
DIAMOND_5 = _NumberCard(Suit.DIAMOND, Number.N_5)
DIAMOND_6 = _NumberCard(Suit.DIAMOND, Number.N_6)
DIAMOND_7 = _NumberCard(Suit.DIAMOND, Number.N_7)
DIAMOND_8 = _NumberCard(Suit.DIAMOND, Number.N_8)
DIAMOND_9 = _NumberCard(Suit.DIAMOND, Number.N_9)
DIAMOND_10 = _NumberCard(Suit.DIAMOND, Number.N_10)
DIAMOND_J = _NumberCard(Suit.DIAMOND, Number.J)
DIAMOND_Q = _NumberCard(Suit.DIAMOND, Number.Q)
DIAMOND_K = _NumberCard(Suit.DIAMOND, Number.K)
CLUB_A = _NumberCard(Suit.CLUB, Number.A)
CLUB_2 = _NumberCard(Suit.CLUB, Number.N_2)
CLUB_3 = _NumberCard(Suit.CLUB, Number.N_3)
CLUB_4 = _NumberCard(Suit.CLUB, Number.N_4)
CLUB_5 = _NumberCard(Suit.CLUB, Number.N_5)
CLUB_6 = _NumberCard(Suit.CLUB, Number.N_6)
CLUB_7 = _NumberCard(Suit.CLUB, Number.N_7)
CLUB_8 = _NumberCard(Suit.CLUB, Number.N_8)
CLUB_9 = _NumberCard(Suit.CLUB, Number.N_9)
CLUB_10 = _NumberCard(Suit.CLUB, Number.N_10)
CLUB_J = _NumberCard(Suit.CLUB, Number.J)
CLUB_Q = _NumberCard(Suit.CLUB, Number.Q)
CLUB_K = _NumberCard(Suit.CLUB, Number.K)
SPADE_A = _NumberCard(Suit.SPADE, Number.A)
SPADE_2 = _NumberCard(Suit.SPADE, Number.N_2)
SPADE_3 = _NumberCard(Suit.SPADE, Number.N_3)
SPADE_4 = _NumberCard(Suit.SPADE, Number.N_4)
SPADE_5 = _NumberCard(Suit.SPADE, Number.N_5)
SPADE_6 = _NumberCard(Suit.SPADE, Number.N_6)
SPADE_7 = _NumberCard(Suit.SPADE, Number.N_7)
SPADE_8 = _NumberCard(Suit.SPADE, Number.N_8)
SPADE_9 = _NumberCard(Suit.SPADE, Number.N_9)
SPADE_10 = _NumberCard(Suit.SPADE, Number.N_10)
SPADE_J = _NumberCard(Suit.SPADE, Number.J)
SPADE_Q = _NumberCard(Suit.SPADE, Number.Q)
SPADE_K = _NumberCard(Suit.SPADE, Number.K)

_NUMBER_CARDS = {
    Suit.HEART: [
        HEART_A,
        HEART_2,
        HEART_3,
        HEART_4,
        HEART_5,
        HEART_6,
        HEART_7,
        HEART_8,
        HEART_9,
        HEART_10,
        HEART_J,
        HEART_Q,
        HEART_K,
    ],
    Suit.DIAMOND: [
        DIAMOND_A,
        DIAMOND_2,
        DIAMOND_3,
        DIAMOND_4,
        DIAMOND_5,
        DIAMOND_6,
        DIAMOND_7,
        DIAMOND_8,
        DIAMOND_9,
        DIAMOND_10,
        DIAMOND_J,
        DIAMOND_Q,
        DIAMOND_K,
    ],
    Suit.CLUB: [
        CLUB_A,
        CLUB_2,
        CLUB_3,
        CLUB_4,
        CLUB_5,
        CLUB_6,
        CLUB_7,
        CLUB_8,
        CLUB_9,
        CLUB_10,
        CLUB_J,
        CLUB_Q,
        CLUB_K,
    ],
    Suit.SPADE: [
        SPADE_A,
        SPADE_2,
        SPADE_3,
        SPADE_4,
        SPADE_5,
        SPADE_6,
        SPADE_7,
        SPADE_8,
        SPADE_9,
        SPADE_10,
        SPADE_J,
        SPADE_Q,
        SPADE_K,
    ],
}

def get_card(suit: Suit, number: Number) -> Card:
    return _NUMBER_CARDS[suit][number.index]


class Deck:
    def __init__(self, jokers: int = 1) -> None:
        cards: list[Card] = []
        for _ in range(jokers):
            cards.append(JOKER)
        for ncs in _NUMBER_CARDS.values():
            for nc in ncs:
                cards.append(nc)
        self._cards = cards

    def random_pick(self, count: int) -> list[Card]:
        if len(self._cards) < count:
            raise ValueError("Not enough cards")
        res = []
        for _ in range(count):
            i = random.randrange(len(self._cards))
            res.append(self._cards.pop(i))
        return res
    
    def append(self, card: Card) -> None:
        self._cards.append(card)

    def extend(self, cards: list[Card]) -> None:
        self._cards.extend(cards)

    def combine(self, deck: 'Deck') -> None:
        self.extend(deck._cards)

    def pop(self, index: int) -> Card:
        return self._cards.pop(index)
