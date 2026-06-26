from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_ESCAPE
from pygame.font import Font

from code.Const import COLOR_YELLOW, SCORE_POSITION, MENU_OPTION, COLOR_WHITE
from code.DBProxy import DBProxy


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save_score(self, menu_return: str, player_score: list[int]):
        pygame.mixer.music.load('./asset/Score.mp3')
        pygame.mixer.music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(text_size=50, text='YOU WINN !!!!!', text_color=COLOR_YELLOW,
                            text_pos=SCORE_POSITION['Title'])
            text = 'Enter your name (3 characters)'
            score = player_score[0]
            if menu_return == MENU_OPTION[0]:
                score = player_score[0]
            if menu_return == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter Team name (3 characters)'
            if menu_return == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter player 1 name (3 characters)'
                else:
                    score = player_score[1]
                    text = 'Enter player 2 name (3 characters)'
            self.score_text(20, text, COLOR_WHITE, SCORE_POSITION['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 3:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show_score()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 3:
                            name += event.unicode
            self.score_text(20, name, COLOR_WHITE, SCORE_POSITION['Name'])
            pygame.display.flip()

    def show_score(self):
        pygame.mixer.music.load('./asset/Score.mp3')
        pygame.mixer.music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', COLOR_YELLOW, SCORE_POSITION['Title'])
        self.score_text(20, 'NAME     SCORE           DATE      ', COLOR_YELLOW, SCORE_POSITION['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}     {score:05d}     {date}', COLOR_YELLOW,
                            SCORE_POSITION[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
                if event.type == pygame.QUIT:
                    pygame.quit()  # close window
                    quit()  # end pygame
            pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
