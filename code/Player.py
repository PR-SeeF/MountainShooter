#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import code.Const as Const
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = Const.ENTITY_SHOT_DELAY[self.name]

    def move(self, ):
        press_key = pygame.key.get_pressed()
        if press_key[Const.PLAYER_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= Const.ENTITY_SPEED[self.name]
        if press_key[Const.PLAYER_DOWN[self.name]] and self.rect.bottom < Const.WINDOW_HEIGHT:
            self.rect.centery += Const.ENTITY_SPEED[self.name]
        if press_key[Const.PLAYER_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= Const.ENTITY_SPEED[self.name]
        if press_key[Const.PLAYER_RIGHT[self.name]] and self.rect.right < Const.WINDOW_WIDTH:
            self.rect.centerx += Const.ENTITY_SPEED[self.name]
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay  <=  0:
            pressed_key = pygame.key.get_pressed()
            if pressed_key[Const.PLAYER_SHOOT[self.name]]:
                self.shot_delay = Const.ENTITY_SHOT_DELAY[self.name]
                return PlayerShot(name = f'{self.name}Shot', position= (self.rect.centerx, self.rect.centery))