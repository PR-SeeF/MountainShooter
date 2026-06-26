#!/usr/bin/python
# -*- coding: utf-8 -*-
from unittest.mock import magic_methods

from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT, MENU_OPTION, ENTITY_HEALTH
from code.Menu import Menu
from code.Level import Level
import pygame

from code.Score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self, ):
        player_score: list[int] = [0, 0]
        player_health: list[int] = [300, 300]
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, 'Level1', menu_return, player_score, player_health)
                level_return = level.run(player_score, player_health)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score, player_health)
                    level_return = level.run(player_score, player_health)
                    if level_return:
                        score.save_score(menu_return, player_score)

            elif menu_return == MENU_OPTION[3]:
                score.show_score()
                pass

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()