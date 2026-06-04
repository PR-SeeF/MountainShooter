import pygame as pg

print('Setup start')
pg.init()
window = pg.display.set_mode((800, 600))
print('Setup end')

print('Looping start')
while (True):

    #event check

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() # close window
            quit() # end pygame
            print('close project')
