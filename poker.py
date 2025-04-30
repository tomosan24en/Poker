from card import *
from abc import ABCMeta, abstractmethod

from card import Card

def _contain_joker(cards: list[Card]) -> int:
    return any(1 if card.is_joker() else 0 for card in cards)

def _count_jokers(cards: list[Card]) -> int:
    return sum(1 if card.is_joker() else 0 for card in cards)

def _group_by_number(cards: list[Card]) -> dict[Number, list[Card]]:
    cards_except_joker = [card for card in cards if not card.is_joker()]
    if not cards_except_joker:
        return {}
    res: dict[Number, list[Card]] = {}
    for i, card in enumerate(cards_except_joker):
        if card.get_number() in res.keys():
            res[card.get_number()].append(card)
        else:
            res[card.get_number()] = [card]
    return res

def _count_groups(gruoping: dict[Number, list[Card]], above: int) -> int:
    return sum(
        1 if len(number_card_list) >= above else 0
        for number_card_list in gruoping.values()
    )


class Hand(metaclass=ABCMeta):
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def check(self, cards: list[Card]) -> bool:
        pass


class _OnePair(Hand):
    def __init__(self) -> None:
        super().__init__("ワンペア", "同じ数字のカードの2枚の組が1組")

    def check(self, cards: list[Card]) -> bool:
        if _contain_joker(cards):
            return True
        
        grouping = _group_by_number(cards)
        return _count_groups(grouping, above=2) >= 1
        

class _TwoPairs(Hand):
    def __init__(self) -> None:
        super().__init__("ツーペア", "同じ数字のカードの2枚の組が2組")

    def check(self, cards: list[Card]) -> bool:
        jokers = _count_jokers(cards)
        if jokers >= 2:
            return True
        groupings = _group_by_number(cards)
        if jokers == 1:
            return len(groupings.keys()) >= 2 and _count_groups(groupings, 2) >= 1
        else:
            return _count_groups(groupings, 2) >= 2
        

class _ThreeCards(Hand):
    def __init__(self) -> None:
        super().__init__("スリーカード", "同じ数字のカードが3枚")

    def check(self, cards: list[Card]) -> bool:
        jokers = _count_jokers(cards)
        if jokers >= 2:
            return True
        groupings = _group_by_number(cards)
        return _count_groups(groupings, 3 - jokers) >= 1
    

ONE_PAIR = _OnePair()
TWO_PAIRS = _TwoPairs()
THREE_CARDS = _ThreeCards()

HANDS = [
    ONE_PAIR,
    TWO_PAIRS,
    THREE_CARDS,
]

for _ in range(10):
    d = Deck(jokers=5).random_pick(5)
    print_card_list(d)
    for hand in HANDS:
        print(hand.name, hand.check(d))
    print("")
