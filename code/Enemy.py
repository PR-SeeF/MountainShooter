#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.EnemyShot import EnemyShot
from code.Entity import Entity
from code.Const import WINDOW_WIDTH, ENTITY_SPEED


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
