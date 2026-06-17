#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION
from code.Menu import Menu
from code.Level import Level
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self, ):
        while True:
            menu: Menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0., 0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)
            elif menu_return == MENU_OPTION[3]:
                pygame.display.flip()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
