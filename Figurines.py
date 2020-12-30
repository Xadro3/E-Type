import pygame
import random

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


class Sprite():
    def __init__(self, xPos, yPos, velocity):

        self.xPos = xPos
        self.yPos = yPos
        self.velocity = velocity
        self.cycle = 0

    def draw(self, screen, image):

        if type(image) == list:

            if self.cycle + 1 >= 30:
                self.cycle = 0
            else:
                self.cycle += 1

            screen.blit(image[self.cycle // 10], (self.xPos, self.yPos))

        else:
            screen.blit(image, (self.xPos, self.yPos))

    def moveDown(self, screen, image):
        if self.yPos + image.get_height() < 480:
            self.yPos = self.yPos + self.velocity
            self.draw(screen, image)
        else:
            self.yPos=0
            self.xPos=random.randrange(0, 440, 5)
            self.draw(screen, image)

    def moveLeft(self, screen, image):
        if self.xPos + image[0].get_width() > 0:
            self.xPos = self.xPos - self.velocity
            self.draw(screen, image)

        else:
            pass

    def moveRight(self, screen, image):
        print(self.xPos)
        if self.xPos + image[0].get_width() < 480:
            self.xPos = self.xPos + self.velocity

            self.draw(screen, image)


        else:
            pass

    def moveUp(self, screen, image):
        if self.yPos + image[0].get_height() > 0:
            self.yPos = self.yPos - self.velocity
            self.draw(screen, image)
        else:
            pass


class Enemy(Sprite):
    def __init__(self, xPos, yPos):
        super(Enemy, self).__init__(xPos, yPos, 2, )

        self.xPos = xPos
        self.yPos = yPos
        self.sprite = loadImage("./Assets/Enemy.png", (255, 255, 255))

    def movingDown(self, screen):
        self.moveDown(screen, self.sprite)


class Player(Sprite):
    def __init__(self, xPos, yPos):
        super(Player, self).__init__(xPos, yPos, 5)

        flyLeft = [loadImage("./Assets/Spaceship links V2.png", (255, 255, 255)),
                   loadImage("./Assets/Spaceship links V21.png", (255, 255, 255)),
                   loadImage("./Assets/Spaceship links V22.png", (255, 255, 255))]
        idling = [loadImage("./Assets/Spaceshipidle.png", (255, 255, 255)),
                loadImage("./Assets/SpaceshipIdle 2.png", (255, 255, 255)),
                loadImage("./Assets/Spaceshipidl3.png", (255, 255, 255))]
        flyRight = [loadImage("./Assets/Spaceship rechts V2.png", (255, 255, 255)),
                    loadImage("./Assets/Spaceship rechts V21.png", (255, 255, 255)),
                    loadImage("./Assets/Spaceship rechts V23.png", (255, 255, 255))]

        self.xPos = xPos
        self.yPos = yPos
        self.cycle = 0
        self.flyleft = flyLeft
        self.idling = idling
        self.flyRight = flyRight

    def movingLeft(self, screen):
        self.moveLeft(screen,self.flyleft)

    def idle(self, screen):
        self.draw(screen,self.idling)

    def movingRight(self, screen):
        self.moveRight(screen,self.flyRight)


class Boolet(Sprite):
    def __init__(self, xPos, yPos):
        super(Boolet, self).__init__(xPos, yPos, 5)

        flying = [loadImage("./Assets/Bullet1.png", (255, 255, 255)),
                  loadImage("./Assets/Bullet2.png", (255, 255, 255)),
                  loadImage("./Assets/Bullet3.png", (255, 255, 255))]

        kaboom = [loadImage("./Assets/explosion 2.png", (255, 255, 255)),
                  loadImage("./Assets/explosion 3.png", (255, 255, 255)),
                  loadImage("./Assets/explosion 4.png", (255, 255, 255))]

        self.kaboom = kaboom
        self.flying = flying
        self.xPos = xPos
        self.yPos = yPos
        self.cycle = 0

    def shot(self, screen):
        self.moveUp(screen, self.flying)

    def bulletHIT(self, screen):
        self.draw(screen, self.kaboom)
