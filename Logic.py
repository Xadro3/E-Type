# Jedes richtig geschriebene wort lässt den Spieler einmal schießen
# Man Hat 3 Leben, wenn die leben 0 erreichen und man nochmal getroffen wird verliert man
# Gewonnen wird mit 250 Punkten, pro getroffenem Gegner 10 Punkte
# GL&HF

import random

import pygame

import Figurines
import game_state


def giveWord(rng, gamestate):
    global data  # Um die performance zu verbessern benutzen wir data als globale variable die immer im speicher geladen ist

    word = gamestate.data[rng]

    return word


def hit(gamestate, screen):
    gs = gamestate

    if gs.flyingShot == 1:  # Checken ob wir eine kugel in der luft haben und hit-abfrage
        gs.bullets[0].shot(screen)
        if gs.bullets[0].yPos - gs.selectedEnemy.yPos < 5:
            gs.flyingShot = 0
            gs.bullets[0].bulletHIT(screen)
            gs.bullets.remove(gs.bullets[0])
            gs.spawnrate += 1
            gs.selectedEnemy.yPos = 0
            gs.score += 10
            pygame.mixer.Sound.play(gs.hitsound)

            if gs.spawnrate % 5 == 1:
                gs.enemies.append(Figurines.Enemy(random.randrange(0, 440, 5), random.randrange(0, 440, 5)))


def findEnemy(gamestate, screen):
    gs = gamestate

    for enemy in gs.enemies:  # Niedrigsten gegner finden
        if enemy.yPos >= gs.selectedEnemy.yPos:
            gs.selectedEnemy = enemy

    if gs.player.xPos > gs.selectedEnemy.xPos:  # Niedrigster gegner in shussbahn bringen
        gs.player.movingLeft(screen)

    elif gs.player.xPos < gs.selectedEnemy.xPos:
        gs.player.movingRight(screen)

    else:
        gs.player.idle(screen)


def lives(gamestate, screen):
    gs = gamestate

    i = len(gamestate.enemies)
    enter = True

    for d in range(i):
        if gs.enemies[d].yPos == gs.player.yPos and gs.enemies[d].xPos == gs.player.xPos:
            gs.healthpoints -= 1
            pygame.mixer.Sound.play(gs.hitsound)
            if gs.healthpoints == -1:  # Game-Over screen
                gs.healthpoints = 3
                screen.blit(Figurines.loadImage("./Assets/spacebg.png"), (0, 0))
                loseText = gs.font.render("You Lose, Press enter To play", False, (40, 100, 255))
                screen.blit(loseText, (5, 240))
                pygame.display.flip()
                pygame.mixer.pause()


                while enter:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gs.running = False
                            enter = False
                            break

                        if event.type == pygame.KEYDOWN:  # Vorbereitung auf neue runde
                            if event.key == pygame.K_RETURN:
                                gs.running = True
                                gs.enemies.clear()
                                gs.enemies = [Figurines.Enemy(random.randrange(0, 440, 5), random.randrange(0, 20)),
                                              Figurines.Enemy(random.randrange(0, 440, 5), random.randrange(0, 20))]
                                gs.selectedEnemy = gs.enemies[1]
                                gs.flyingShot = 0
                                gs.inputbox = ""
                                gs.newWord = "resume"
                                gs.score = 0
                                gs.bullets.clear()
                                pygame.mixer.unpause()
                                enter = False
                                break

            gs.clock.tick(60)
        if enter == False:
            break


def userInterface(gamestate, screen):
    gs = gamestate

    pygame.draw.rect(screen, (40, 100, 255), (0, 0, 480, 40))
    words = gs.font.render(gs.newWord, False, 120, (40, 100, 255))  # scoreboard, input, output rendern
    scorerender = gs.font.render(str(gs.score), False, 120, (40, 100, 255))
    inputrender = gs.font.render(gs.inputbox, False, 120, (40, 100, 255))
    liverender = gs.font.render(str(gs.healthpoints), False, 120, (40, 100, 255))
    screen.blit(words, (3, 3))
    screen.blit(scorerender, (440, 3))
    screen.blit(liverender, (1, 454))
    screen.blit(inputrender, (0, 40))


def restofthelogic(gamestate, screen):
    gs = gamestate

    for event in pygame.event.get():  # Event abfrage,

        if event.type == pygame.QUIT:
            gs.running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

            elif event.key == pygame.K_BACKSPACE and len(gs.inputbox) != 0:

                gs.inputbox = ""

            else:
                pygame.mixer.Sound.play(gs.input)
                gs.inputbox += event.unicode

    if gs.inputbox == gs.newWord:
        if gs.flyingShot != 1 and gs.player.xPos == gs.selectedEnemy.xPos:
            pygame.mixer.Sound.play(gs.shot)
            gs.bullets.append(Figurines.Boolet(gs.player.xPos, gs.player.yPos))
            gs.flyingShot = 1
            gs.newWord = (giveWord(random.randrange(0, 370100), gamestate))
            gs.inputbox = ""


def game():
    gamestate = game_state.GameState

    pygame.mixer.music.load("./Assets/sounds/loop.mp3")
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.play(-1)
    screen = gamestate.screen

    # gameloop

    while gamestate.running:

        gamestate.clock.tick(45)

        screen.fill((255, 255, 255))
        screen.blit(gamestate.bg, (0, 0))

        for d in gamestate.enemies:
            d.movingDown(screen)

        findEnemy(gamestate, screen)
        hit(gamestate, screen)
        lives(gamestate, screen)
        userInterface(gamestate, screen)
        restofthelogic(gamestate, screen)

        pygame.display.flip()


game()

# Sountrack made by frostfire64#2701
# https://github.com/dwyl/english-words --> Wörterbuch
# der https://www.pixilart.com/8-bit-adventure/gallery Artist für Background, Schiffe und Animationen Eigenproduktion
# https://www.reddit.com/r/PixelArt/comments/bcvvd1/oc_space_time/ direkter link für Background
# Font in Font ordner mit credits
# SPGLOBAL INC.
