# Classe Game

import pygame

from code.Conts import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # Criando a Janela do Jogo

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



