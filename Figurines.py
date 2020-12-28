import pygame


def loadImage(filename, colorkey=None):
    image = pygame.image.load(filename)

    if image.get_alpha() == None:
        image = image.convert()
    else:
        image = image.convert_alpha()

    if colorkey != None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)

    return image


def draw(screen, xPos, yPos, image):
        screen.blit(image,(xPos, yPos))


class Enemy():
    def __init__(self,xPos,yPos):

        self.xPos = xPos
        self.yPos = yPos
        self.sprite = loadImage("./Assets/Enemy.png",(255,255,255))

    def moveDown(self,screen):
        if self.yPos+self.sprite.get_height() < 480:
            self.yPos = self.yPos + 1
        else:
            self.yPos = 0
            if self.xPos+self.sprite.get_width() < 480:
                self.xPos = self.xPos + 50
            else:
                self.xPos = 0
        draw(screen,self.xPos,self.yPos,self.sprite)

class Player:
    def __init__(self,xPos, yPos):

       self.xPos = xPos
       self.yPos = yPos
       self.cycle = 0

    def moveLeft(self, screen):
        flyLeft = [loadImage("./Assets/Spaceship links V2.png",(255,255,255)),
                   loadImage("./Assets/Spaceship links V21.png",(255,255,255)),
                   loadImage("./Assets/Spaceship links V22.png",(255,255,255))]

        if self.cycle+1>=300: #Animation
            self.cycle=0
        else:
            self.cycle+=1
        self.xPos = self.xPos - 5
        draw(screen,self.xPos,self.yPos,flyLeft[self.cycle//100])

    def idle(self, screen):
        idle = [loadImage("./Assets/Spaceshipidle.png",(255,255,255)),
                loadImage("./Assets/SpaceshipIdle 2.png",(255,255,255)),
                loadImage("./Assets/Spaceshipidl3.png",(255,255,255))]

        if self.cycle+1>=30:
            self.cycle=0
        else:
            self.cycle+=1

        draw(screen,self.xPos,self.yPos,idle[self.cycle//10])

    def moveRight(self, screen):
        flyRight = [loadImage("./Assets/Spaceship rechts V2.png",(255,255,255)),
                    loadImage("./Assets/Spaceship rechts V21.png",(255,255,255)),
                    loadImage("./Assets/Spaceship rechts V23.png",(255,255,255))]

        if self.cycle+1>=300:
            self.cycle=0
        else:
            self.cycle+=1

        self.xPos = self.xPos + 5
        draw(screen,self.xPos, self.yPos,flyRight[self.cycle//100])

    def shoot(self, ammo):
        if(ammo!=0):
            ammo-1
            return ammo

class Boolet():
    def __init__(self, xPos, yPos):
        self.xPos=xPos
        self.yPos=yPos
        self.cycle=0

    def shot(self, screen):

        flying=[loadImage("./Assets/Bulle1.png",(255,255,255)),loadImage("./Assets/Bulle2.png",(255,255,255))]

        if self.yPos + flying[0].get_height() > 0:
            self.yPos = self.yPos - 2

        if round(self.cycle)==0:
            self.cycle += 0.1
        else:
            self.cycle -=0.1

        draw(screen,self.xPos,self.yPos,flying[round(self.cycle)])

    def bulletHIT(self, screen):

        self.cycle = 0

        kaboom = [loadImage("./Assets/exlposion 1.png",(255,255,255)),
                  loadImage("./Assets/explosion 2.png",(255,255,255)),
                  loadImage("./Assets/explsion 3.png",(255,255,255)),
                  loadImage("./Assets/explsion 4.png",(255,255,255))]
        while self.cycle <=3:

            self.cycle+=0.1

            draw(screen,self.xPos, self.yPos,kaboom[round(self.cycle)])


