#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Enemy import Enemy
from code.Player import Player
from code.Background import Background
from code.Const import WINDOW_WIDTH, WINDOW_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WINDOW_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player(name='Player1', position=(10, WINDOW_HEIGHT / 2 - 30))
            case 'Player2':
                return Player(name='Player2', position=(10, WINDOW_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy(name='Enemy1', position=(WINDOW_WIDTH + 10, random.randint(5, WINDOW_HEIGHT)))
            case 'Enemy2':
                return Enemy(name='Enemy2', position=(WINDOW_WIDTH + 10, random.randint(5, WINDOW_HEIGHT)))
