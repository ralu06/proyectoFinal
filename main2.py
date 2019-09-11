import pygame as pg
from pygame.locals import *
import sys, os
import random

_fps = 60



class Nave(pg.sprite.Sprite):
    x = 0
    y = 0
    velocidad = 5
    diry = 1

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(os.getcwd()+"/assets/rocket.png")
        self.rect = self.image.get_rect()

    def avanza(self):
        if self.y <= 0:
            self.diry = -1
        
        if self.y >= 400:
            self.diry = 1

        self.y += self.diry * self.velocidad

class Meteorito(pg.sprite.Sprite):
    x = 1150
    y = random.randrange(5,120)
    velocidad = random.randrange(4, 7)
    dirx = random.randint(1, 1)
    diry = random.randint(0, 0)

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(os.getcwd()+"/assets/comet.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.x += self.dirx * self.velocidad
        self.y += self.diry * self.velocidad

        if self.x >= 1000:
            self.dirx = -1
           
        if self.y >= 700:
            self.diry = 0
        
        self.rect.x = self.x
        self.rect.y = self.y
            
class Meteorito2(pg.sprite.Sprite):
    x = 1150
    y = random.randrange(150,200)
    velocidad = random.randrange(1, 4)
    dirx = random.randint(1, 1)
    diry = random.randint(0, 0)

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(os.getcwd()+"/assets/comet.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.x += self.dirx * self.velocidad
        self.y += self.diry * self.velocidad

        if self.x >= 1000:
            self.dirx = -1
           
        if self.y >= 700:
            self.diry = 0
        
        self.rect.x = self.x
        self.rect.y = self.y

class Meteorito3(pg.sprite.Sprite):
    x = 1150
    y = random.randrange(250,400)
    velocidad = random.randrange(3, 6)
    dirx = random.randint(1, 1)
    diry = random.randint(0, 0)

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(os.getcwd()+"/assets/comet.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.x += self.dirx * self.velocidad
        self.y += self.diry * self.velocidad

        if self.x >= 1000:
            self.dirx = -1
           
        if self.y >= 700:
            self.diry = 0
        
        self.rect.x = self.x
        self.rect.y = self.y

class Meteorito4(pg.sprite.Sprite):
    x = 1150
    y = random.randrange(420,600)
    velocidad = random.randrange(1, 4)
    dirx = random.randint(1, 1)
    diry = random.randint(0, 0)

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(os.getcwd()+"/assets/comet.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.x += self.dirx * self.velocidad
        self.y += self.diry * self.velocidad

        if self.x >= 1000:
            self.dirx = -1
           
        if self.y >= 700:
            self.diry = 0
        
        self.rect.x = self.x
        self.rect.y = self.y

class Meteorito5(pg.sprite.Sprite):
    x = 1150
    y = random.randrange(615,715)
    velocidad = random.randrange(2, 5)
    dirx = random.randint(1, 1)
    diry = random.randint(0, 0)

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(os.getcwd()+"/assets/comet.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.x += self.dirx * self.velocidad
        self.y += self.diry * self.velocidad

        if self.x >= 1000:
            self.dirx = -1
           
        if self.y >= 700:
            self.diry = 0
        
        self.rect.x = self.x
        self.rect.y = self.y

class Game:
    clock = pg.time.Clock()

    def __init__(self, width, height):
        self.display = pg.display
        self.screen = self.display.set_mode((width, height))
        
        self.display.set_caption('The quest')

        self.meteorito = Meteorito()
        self.meteorito2 = Meteorito2()
        self.meteorito3 = Meteorito3()
        self.meteorito4 = Meteorito4()
        self.meteorito5 = Meteorito5()

        self.player = Nave()
        self.player.x = 100
        self.player.y = 200

        self.allSprites = pg.sprite.Group()

        self.allSprites.add(self.meteorito)
        self.allSprites.add(self.meteorito2)
        self.allSprites.add(self.meteorito3)
        self.allSprites.add(self.meteorito4)
        self.allSprites.add(self.meteorito5)

        self.allSprites.add(self.player)

      
    def handleevent(self):
        for event in pg.event.get():
            if event.type == QUIT:
                self.gameover() 
            
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    self.player.diry = -1
                    self.player.velocidad = 5
                    self.player.avanza()

                if event.key == K_DOWN:
                    self.player.diry = 1
                    self.player.velocidad = 5
                    self.player.avanza()

        keys_pressed = pg.key.get_pressed()
        if keys_pressed[K_UP]:
            self.player.diry = -1
            if self.player.velocidad < 15:
                self.player.velocidad += 1
            self.player.avanza()

        if keys_pressed[K_DOWN]:
            self.player.diry = 1
            if self.player.velocidad < 15:
                self.player.velocidad += 1
            self.player.avanza() 

    def start(self):
        game_over = False
        while not game_over:
            self.clock.tick(_fps)
            self.handleevent()

            for event in pg.event.get():
                if event.type == QUIT:
                    pg.quit()
                    sys.exit()

            self.screen.fill((0, 100, 60))

            self.allSprites.update()
            self.allSprites.draw(self.screen)


            self.display.flip()

        pg.quit()
        sys.exit()

if __name__ == '__main__':
    pg.init()
    game = Game(1200,730)
    game.start()