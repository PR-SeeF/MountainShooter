#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from pygame.font import Font

import pygame
from pygame import quit, Surface, Rect

from code.Enemy import Enemy
from code.EntityMediator import EntityMediator
from code.Const import COLOR_WHITE, WINDOW_HEIGHT, MENU_OPTION, EVENT_ENEMY, COLOR_GREEN, COLOR_CIAN
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.Player import Player
from code.PlayerShot import PlayerShot


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 sec
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 3000)

    def run(self):
        pygame.mixer.music.load(f'./asset/{self.name}.mp3')
        pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        while True:
            self.window.fill((0, 0, 0))
            clock.tick(60)
            for ent in self.entity_list:
                ent.move()
                self.window.blit(source=ent.surf, dest=ent.rect)

                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 : {ent.health} | Score: {ent.score}', COLOR_GREEN, (10, 30))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player2 : {ent.health} | Score: {ent.score}', COLOR_CIAN, (10, 40))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy2', 'Enemy1'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 : .1f}s', COLOR_WHITE, (10, 15))
            self.level_text(14, f'fps: {clock.get_fps(): .0f}s', COLOR_WHITE, (10, WINDOW_HEIGHT - 35))
            self.level_text(14, f'entidades {len(self.entity_list)}', COLOR_WHITE, (10, WINDOW_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.verify_collision(entity_List=self.entity_list)
            EntityMediator.verify_health(entity_List=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
