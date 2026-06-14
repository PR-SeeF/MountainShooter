# C
import pygame

COLOR_ORANGE = (255, 128, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 255, 0)

# E
ENTITY_HEALTH = {'Level1Bg0': 999,
                 'Level1Bg1': 999,
                 'Level1Bg2': 999,
                 'Level1Bg3': 999,
                 'Level1Bg4': 999,
                 'Level1Bg5': 999,
                 'Level1Bg6': 999,
                 'Player1': 300,
                 'Player2': 300,
                 'Enemy1': 50,
                 'Enemy2': 70,
                 'Player1Shot': 1,
                 'Player2Shot': 1,
                 'Enemy1Shot': 1,
                 'Enemy2Shot': 1,
                 }

ENTITY_SHOT_DELAY = {'Player1': 20,
                     'Player2': 20,
                     'Enemy1': 30,
                     'Enemy2': 20,
                     }

ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 1,
                'Level1Bg2': 2,
                'Level1Bg3': 3,
                'Level1Bg4': 4,
                'Level1Bg5': 5,
                'Level1Bg6': 6,
                'Player1': 4,
                'Player2': 4,
                'Enemy1': 3,
                'Enemy2': 2,
                'Player1Shot': 2,
                'Player2Shot': 2,
                'Enemy1Shot': 4,
                'Enemy2Shot': 4 ,
                }

EVENT_ENEMY = pygame.USEREVENT + 1

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - CO-OP',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
# P

PLAYER_UP = {'Player1': pygame.K_UP,
             'Player2': pygame.K_w}
PLAYER_DOWN = {'Player1': pygame.K_DOWN,
               'Player2': pygame.K_s}
PLAYER_LEFT = {'Player1': pygame.K_LEFT,
               'Player2': pygame.K_a}
PLAYER_RIGHT = {'Player1': pygame.K_RIGHT,
                'Player2': pygame.K_d}
PLAYER_SHOOT = {'Player1': pygame.K_RCTRL,
                'Player2': pygame.K_BACKSPACE}
# W
WINDOW_WIDTH = 576
WINDOW_HEIGHT = 324
