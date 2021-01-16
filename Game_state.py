import random

import pygame

import Figurines


class GameState():
    # wir packen alle unseren schönen variablen in eine klasse um sie einfach in der gegend herumschieben können
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("E-Type")
    pygame.display.set_icon(Figurines.loadImage("./Assets/Spaceship.png", (255, 255, 255)))
    pygame.mouse.set_visible(True)
    random.seed()
    enemies = [Figurines.Enemy(random.randrange(0, 440, 5), random.randrange(0, 20)),
               Figurines.Enemy(random.randrange(0, 440, 5), random.randrange(0, 20))]
    player = Figurines.Player(240, 448)
    bullets = []
    selectedEnemy = enemies[1]
    flyingShot = 0
    healthpoints = 1
    score = 0
    spawnrate = 0
    running = True
    clock = pygame.time.Clock()
    newWord = "start"
    inputbox = ""
    # Assetloading
    font = pygame.font.Font("./Assets/font/font.TTF", 20)
    hitsound = pygame.mixer.Sound("./Assets/sounds/xplod.wav")
    shot = pygame.mixer.Sound("./Assets/sounds/laser.wav")
    input = pygame.mixer.Sound("./Assets/sounds/input.wav")
    bg = Figurines.loadImage("./Assets/spacebg.png")
    pygame.mixer.Sound.set_volume(hitsound,0.008)
    pygame.mixer.Sound.set_volume(shot, 0.008)
    pygame.mixer.Sound.set_volume(input, 0.008)
    with open(
            "./Assets/oxford.txt") as word_file:
        data = list(word_file.read().split())
