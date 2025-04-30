import pyxel
from card import *


JOKER_POS = (0, 32)
MARK_POS = {
    Suit.SPADE: (0, 0),
    Suit.CLUB: (16, 0),
    Suit.HEART: (32, 0),
    Suit.DIAMOND: (48, 0),
}


def draw_card(x: float, y: float, card: Card) -> None:
    if card.is_joker():
        pyxel.blt(x, y, 0, JOKER_POS[0], JOKER_POS[1], 16, 24, colkey=pyxel.COLOR_BLACK)
    else:
        number_x = 16 * (card.get_number().index)
        number_y = 16 if (card.get_suit() in [Suit.CLUB, Suit.SPADE]) else 24
        pyxel.blt(x, y, 0, number_x, number_y, 16, 8, colkey=pyxel.COLOR_BLACK)
        mark_pos = MARK_POS[card.get_suit()]
        pyxel.blt(x, y + 8, 0, mark_pos[0], mark_pos[1], 16, 16, pyxel.COLOR_BLACK)
        
    
def draw_card_back(x: float, y: float) -> None:
    pyxel.blt(x, y, 0, 16, 32, 16, 24, colkey=pyxel.COLOR_BLACK)


def draw_change_mark(x: float, y: float) -> None:
    pyxel.blt(x, y, 0, 32, 32, 8, 8, pyxel.COLOR_BLACK)


X_LIST = [
    40 + i * 24
    for i in range(5)
]


class App:
    def __init__(self) -> None:
        pyxel.init(200, 200, title="Poker")
        pyxel.load("./resource.pyxres")
        self.initialize()
        pyxel.run(self.update, self.draw)

    def initialize(self) -> None:
        self.width = 200
        self.height = 200
        self.deck = Deck()
        self.dealt_cards = self.deck.random_pick(5)
        self.cursor = 0
        self.change = [False for _ in range(5)]

    def update(self) -> None:
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.cursor = max(0, self.cursor - 1)
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.cursor = min(4, self.cursor + 1)
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.change[self.cursor] = not self.change[self.cursor]

    def draw(self) -> None:
        self._draw_background()
        draw_card_back(10, 10)

        for i, card in enumerate(self.dealt_cards):
            draw_card(X_LIST[i], 10, card)
            if self.change[i]:
                draw_change_mark(X_LIST[i] + 4, 36)

        pyxel.rectb(X_LIST[self.cursor] - 1, 9, 18, 26, pyxel.COLOR_YELLOW)

    def _draw_background(self) -> None:
        pyxel.cls(pyxel.COLOR_GREEN)
        pyxel.rectb(1, 1, self.width - 2, self.height - 2, pyxel.COLOR_LIME)

App()
