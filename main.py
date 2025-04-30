import pyxel
from card import *


class App:
    def __init__(self) -> None:
        pyxel.init(200, 200, title="Poker")
        pyxel.load("./resource.pyxres")
        self.initialize()
        pyxel.run(self.update, self.draw)

    def initialize(self) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass


App()
