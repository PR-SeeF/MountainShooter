#!/usr/bin/python
# -*- coding: utf-8 -*-
from operator import truediv

import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WINDOW_WIDTH, COLOR_WHITE, COLOR_ORANGE, MENU_OPTION


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer.music.load('./asset/Menu.mp3')
        pygame.mixer.music.play(-1)

        while True:

            self.menu_text(text_size=50, text_color=COLOR_ORANGE, text="MOUNTAIN",
                           text_center_pos=((WINDOW_WIDTH / 2), 70))
            self.menu_text(text_size=50, text_color=COLOR_ORANGE, text="SHOOTER",
                           text_center_pos=((WINDOW_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i], text_color=COLOR_WHITE, text_center_pos=((WINDOW_WIDTH / 2), 200 + i * 20))


            pygame.display.flip()
            # event check
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
                    print('close project')

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
