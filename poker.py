from card import *
from abc import ABCMeta, abstractmethod

from card import Card


class DealtCards:
    def __init__(self, cards: list[Card]) -> None:
        self.cards = cards
        self._jokers = sum(1 if card.is_joker() else 0 for card in self.cards)

        cards_except_joker = [card for card in self.cards if not card.is_joker()]

        grouping_number: dict[Number, list[Card]] = {}
        for i, card in enumerate(cards_except_joker):
            if card.get_number() in grouping_number.keys():
                grouping_number[card.get_number()].append(card)
            else:
                grouping_number[card.get_number()] = [card]
        self._grouping_number = grouping_number

        grouping_suit: dict[Suit, list[Card]] = {}
        for i, card in enumerate(cards_except_joker):
            if card.get_suit() in grouping_suit.keys():
                grouping_suit[card.get_suit()].append(card)
            else:
                grouping_suit[card.get_suit()] = [card]
        self._grouping_suit = grouping_suit

    def contains_joker(self) -> int:
        return self._jokers >= 1

    def count_joker(self) -> int:
        return self._jokers

    def group_by_number(self) -> dict[Number, list[Card]]:
        return self._grouping_number
    
    def count_distinct_numbers(self) -> int:
        return len(self._grouping_number.keys())

    def count_number_groups(self, above: int) -> int:
        return sum(
            1 if len(number_card_list) >= above else 0
            for number_card_list in self._grouping_number.values()
        )
    
    def count_distinct_suits(self) -> int:
        return len(self._grouping_suit.keys())


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
        return cards.count_number_groups(2) >= 1
        

class _TwoPairs(Hand):
    def __init__(self) -> None:
        super().__init__("ツーペア", "同じ数字のカードの2枚の組が2組")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 2:
            return True
        if jokers == 1:
            return cards.count_distinct_numbers() >= 2 and cards.count_number_groups(2) >= 1
        else:
            return cards.count_number_groups(2) >= 2
        

class _ThreeCards(Hand):
    def __init__(self) -> None:
        super().__init__("スリーカード", "同じ数字のカードが3枚")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 2:
            return True
        return cards.count_number_groups(3 - jokers) >= 1
    

class _FullHouse(Hand):
    def __init__(self) -> None:
        super().__init__("フルハウス", "同じ数字のカードの3枚の組と2枚の組が一つずつ")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 3:
            return True
        if jokers == 2:
            return cards.count_distinct_numbers() <= 2
        if jokers == 1:
            return cards.count_distinct_numbers() == 2
        else:
            return cards.count_distinct_numbers() == 2 and cards.count_number_groups(2) == 2


class _FourCards(Hand):
    def __init__(self) -> None:
        super().__init__("フォーカード", "同じ数字のカードが4枚")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 3:
            return True
        return cards.count_number_groups(4 - jokers) >= 1
    

class _FiveCards(Hand):
    def __init__(self) -> None:
        super().__init__("ファイブカード", "同じ数字のカードが5枚")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 4:
            return True
        return cards.count_number_groups(5 - jokers) >= 1
    

class _Flush(Hand):
    def __init__(self) -> None:
        super().__init__("フラッシュ", "同じマークのカードが5枚")

    def check(self, cards: DealtCards) -> bool:
        return cards.count_distinct_suits() == 1
    

class _Straight(Hand):
    def __init__(self) -> None:
        super().__init__("ストレート", "2からAの中で連続した5つの数字")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 4:
            return True
        numbers_strength = sorted(map(lambda number: number.strength_A, cards.group_by_number().keys())) # 弱い順
        diff = numbers_strength[-1] - numbers_strength[0]
        return diff <= 4 and cards.count_distinct_numbers() == 5 - jokers
    

class _StraightFlush(Hand):
    def __init__(self) -> None:
        super().__init__("ストレートフラッシュ", "フラッシュかつストレート")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 4:
            return True
        numbers_strength = sorted(map(lambda number: number.strength_A, cards.group_by_number().keys())) # 弱い順
        diff = numbers_strength[-1] - numbers_strength[0]
        straight = (diff <= 4 and cards.count_distinct_numbers() == 5 - jokers)
        flush = (cards.count_distinct_suits() == 1)
        return straight and flush
    

class _RoyalFlush(Hand):
    def __init__(self) -> None:
        super().__init__("ロイヤルストレートフラッシュ", "数字が10,J,Q,K,Aのストレートフラッシュ")

    def check(self, cards: DealtCards) -> bool:
        jokers = cards.count_joker()
        if jokers >= 4:
            return True
        numbers_strength = sorted(map(lambda number: number.strength_A, cards.group_by_number().keys())) # 弱い順
        print(numbers_strength)
        diff = numbers_strength[-1] - numbers_strength[0]
        royal = (numbers_strength[0] >= Number.N_10.strength_A and numbers_strength[-1] <= Number.A.strength_A)
        straight = (diff <= 4 and cards.count_distinct_numbers() == 5 - jokers)
        flush = (cards.count_distinct_suits() == 1)
        return royal and straight and flush
    

ONE_PAIR = _OnePair()
TWO_PAIRS = _TwoPairs()
THREE_CARDS = _ThreeCards()
FULL_HOUSE = _FullHouse()
FOUR_CARDS = _FourCards()
FIVE_CARDS = _FiveCards()
FLUSH = _Flush()
STRAIGHT = _Straight()
STRAIGHT_FLUSH = _StraightFlush()
ROYAL_FLUSH = _RoyalFlush()

HANDS: list[Hand] = [
    ONE_PAIR,
    TWO_PAIRS,
    THREE_CARDS,
    FULL_HOUSE,
    FOUR_CARDS,
    FIVE_CARDS,
    FLUSH,
    STRAIGHT,
    STRAIGHT_FLUSH,
    ROYAL_FLUSH
]
