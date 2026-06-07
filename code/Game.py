#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self, ):
        while True:
            menu: Menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = level(self.window, 'level1', menu_return)
                menu_return = level.run()
            elif menu_return == MENU_OPTION[3]:
                pygame.display.flip()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()


