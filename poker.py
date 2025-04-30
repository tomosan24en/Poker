from card import *
from abc import ABCMeta, abstractmethod

from card import Card


class DealtCards:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards
        self._jokers = sum(1 if card.is_joker() else 0 for card in self.cards)

        grouping: dict[Number, list[Card]] = {}
        cards_except_joker = [card for card in self.cards if not card.is_joker()]
        for i, card in enumerate(cards_except_joker):
            if card.get_number() in grouping.keys():
                grouping[card.get_number()].append(card)
            else:
                grouping[card.get_number()] = [card]
        self._grouping = grouping

    def contains_joker(self) -> int:
        return self._jokers >= 1

    def count_joker(self) -> int:
        return self._jokers

    def group_by_number(self) -> dict[Number, list[Card]]:
        return self._grouping
    
    def count_distinct_numbers(self) -> int:
        return len(self._grouping.keys())

    def count_groups(self, above: int) -> int:
        return sum(
            1 if len(number_card_list) >= above else 0
            for number_card_list in self._grouping.values()
        )


class Hand(metaclass=ABCMeta):
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @abstractmethod
    def check(self, cards: DealtCards) -> bool:
        pass


class _OnePair(Hand):
    def __init__(self) -> None:
        super().__init__("ワンペア", "同じ数字のカードの2枚の組が1組")

    def check(self, cards: DealtCards) -> bool:
        if cards.contains_joker():
            return True
        return cards.count_groups(2) >= 1
        

class _TwoPairs(Hand):
    def __init__(self) -> None:
        super().__init__("ツーペア", "同じ数字のカードの2枚の組が2組")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 2:
            return True
        if jokers == 1:
            return cards.count_distinct_numbers() >= 2 and cards.count_groups(2) >= 1
        else:
            return cards.count_groups(2) >= 2
        

class _ThreeCards(Hand):
    def __init__(self) -> None:
        super().__init__("スリーカード", "同じ数字のカードが3枚")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 2:
            return True
        return cards.count_groups(3 - jokers) >= 1
    

ONE_PAIR = _OnePair()
TWO_PAIRS = _TwoPairs()
THREE_CARDS = _ThreeCards()

HANDS: list[Hand] = [
    ONE_PAIR,
    TWO_PAIRS,
    THREE_CARDS,
]

for _ in range(10):
    d = DealtCards(Deck(jokers=5).random_pick(5))
    print_card_list(d.cards)
    for hand in HANDS:
        print(hand.name, hand.check(d))
    print("")
