import pygame as pg
from pygame.locals import *
import sys, os
import random

_fps = 60

def titulo():
    pygame.font.SysFont('tehquest', 30, bold=False, italic=False)
    return Font


class Game:
    clock = pg.time.Clock()
   
    def __init__(self, width, height):
        self.display = pg.display
        self.screen = self.display.set_mode((width, height))       
        self.display.set_caption('The quest')





    def start(self):
        while True:       
            self.clock.tick(_fps)

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            self.display.flip()


if __name__ == '__main__':
    pg.init()
    game = Game(1200,730)
game.start()