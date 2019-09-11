
import pygame as pg
from pygame.locals import *
import sys, os
import random

_fps=60

class Meteorito(pg.sprite.Sprite):
    x = 0
    y = 0
    w = 16
    h = 16
    color = (255, 255, 255)
    velocidad = 5
    dirx = 1
    diry = 1

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.getcwd()+"/assets/comet.png")
        self.rect = self.image.get_rect()
        

class Game: 
    clock = pg.time.Clock()

    def __init__(self, width, height):
        self.size = (width, height)
        self.display = pg.display
        self.screen = self.display.set_mode(self.size)
        self.screen.fill((60, 60, 60))
        self.display.set_caption('The Quest')

        self.meteorito = Meteorito()

    def iniciopartida(self):
        self.meteorito.x = 400
        self.meteorito.y = 200
        self.meteorito.diry = random.choice([-1,1])
        self.meteorito.dirx = 500
        self.meteorito.velocidad = random.randrange(5, 11)
       

    def start(self):

        while True:
            self.clock.tick(_fps)                   
            
    

if __name__ == '__main__':
    pg.init()
    game = Game(1000, 700)
game.start()        
        