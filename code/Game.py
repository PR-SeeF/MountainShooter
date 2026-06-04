#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT
from code.Menu import Menu
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self, ):
        while True:
            menu: Menu = Menu(self.window)
            menu.run()
            pass


