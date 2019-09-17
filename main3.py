import pygame as pg
from pygame.locals import *
import sys, os
import random

_fps = 60

class Nave(pg.sprite.Sprite):
    x = 0
    y = 0
    w = 16
    h = 100
    velocidad = 5
    diry = 1

    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = pg.image.load(os.getcwd()+"/assets/rocket.png")
        self.rect = self.image.get_rect()

    def avanza(self):
        self.y += self.diry * self.velocidad

        if self.y <=0:
            self.y = 0
 
        if self.y >= 730 - self.h:
            self.y = 730 - self.h

    def watch(self):
        if self.sigueA:
            if self.sigueA.x <= 400:
                deltaY = self.sigueA.y - self.y
                if deltaY > 0: 
                    self.diry = +1
                elif deltaY < 0:
                    self.diry = -1
                else:
                    self.diry = 0
                self.avanza()

    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y

    def comprobarChoque(self, spriteGroup):
        if pg.sprite.spritecollide(self, spriteGroup, False):
            self.dirx = self.dirx * -1
            self.x += self.dirx * self.w

            if self.velocidad <= 14:
                self.velocidad += 0.5 

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
    y = random.randrange(615,640)
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

        self.allSprites = pg.sprite.Group()
        self.playersGroup = pg.sprite.Group()

        self.meteorito = Meteorito()
        self.meteorito2 = Meteorito2()
        self.meteorito3 = Meteorito3()
        self.meteorito4 = Meteorito4()
        self.meteorito5 = Meteorito5()

        self.player = Nave()
        self.playersGroup.add(self.player)


        self.allSprites.add(self.meteorito)
        self.allSprites.add(self.meteorito2)
        self.allSprites.add(self.meteorito3)
        self.allSprites.add(self.meteorito4)
        self.allSprites.add(self.meteorito5)

        self.allSprites.add(self.player)

        self.player.comprobarChoque(self.meteorito)
        self.player.comprobarChoque(self.meteorito2)
        self.player.comprobarChoque(self.meteorito3)
        self.player.comprobarChoque(self.meteorito4)
        self.player.comprobarChoque(self.meteorito5)
        


    def gameover(self):
        pg.quit()
        sys.exit()
      
    def movement(self):
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

    def render(self):
        
        self.screen.fill((100,50,100))

        self.allSprites.update()
        self.allSprites.draw(self.screen)

        self.display.flip()

    def start(self):
        while True:
       
            self.clock.tick(_fps)
        
            self.movement()

            self.render()

if __name__ == '__main__':
    pg.init()
    game = Game(1200,730)
game.start()