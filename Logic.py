#Jedes richtig geschriebene wort gibt eine "Kugel" im magazin, mit enter wird geschossen, worte sind nicht Case-Sensitive
#Man Hat 3 bomben mit dehnen einem nicht ageschossener gegner eliminiert wird, bei 0 bomben führt der  nächste gegner zum Game-Over
#Gewonnen wird mit 1.000.000 Punkten
#GL&HF
import pygame
import Figurines
import random

with open(
        "./Assets/oxford.txt") as word_file:  # Wir suchen uns auf basis eines zufallsgenerators ein wort aus unserer liste
     data = list(word_file.read().split())

def giveWord(rng):
        global data #Um die performance zu verbessern benutzen wir data als globale variable die immer im speicher geladen ist

        word =data[rng]

        return word


def game():
    pygame.init()
    screen = pygame.display.set_mode((480, 480))
    pygame.display.set_caption("E-Type")
    pygame.display.set_icon(Figurines.loadImage("./Assets/Spaceship.png",(255,255,255)))
    pygame.mouse.set_visible(True)
    random.seed()
    healthpoints = 3
    score = 0
    spawnrate = 0
    newWord = "Start"
    font = pygame.font.Font("./Assets/font/font.TTF", 20)
    inputbox=""

    clock = pygame.time.Clock()
    bg = Figurines.loadImage("./Assets/spacebg.png")

    enemies = [Figurines.Enemy(random.randrange(0,440,5), random.randrange(0,20)), Figurines.Enemy(random.randrange(0,440,5), random.randrange(0,20))]
    player=Figurines.Player(320,448)
    bullets = []
    selectedEnemy = enemies[1]
    flyingShot = 0

    running = True
    while running:
        clock.tick(45)

        screen.fill((255,255,255))
        screen.blit(bg,(0,0))


        for d in enemies:
            d.moveDown(screen)

        for enemy in enemies:       #Niedrigsten gegner finden
            if enemy.yPos >= selectedEnemy.yPos:
                selectedEnemy = enemy







        if player.xPos > selectedEnemy.xPos: #Niedrigster gegner in shussbahn bringen
            player.moveLeft(screen)

        elif player.xPos < selectedEnemy.xPos:
            player.moveRight(screen)

        else:
            player.idle(screen)



        if flyingShot == 1:     #Checken ob wir eine kugel in der luft haben und hit-abfrage
            bullets[0].shot(screen)
            if bullets[0].yPos - selectedEnemy.yPos<5:
                flyingShot = 0
                bullets[0].bulletHIT(screen)
                bullets.remove(bullets[0])
                spawnrate +=1
                selectedEnemy.yPos = 0
                score+=10
                if spawnrate%5==1:
                    enemies.append(Figurines.Enemy(random.randrange(0,440,5),0))


        i=len(enemies)      #Game-Overscreen
        enter = True
        for d in range(i):

            if enemies[d].yPos == player.yPos and enemies[d].xPos == player.xPos:
                healthpoints -=1
                if healthpoints == -1:
                    healthpoints = 3
                    screen.blit(Figurines.loadImage("./Assets/spacebg.png"), (0, 0))
                    loseText = font.render("You Lose, Press enter To play",False,(40, 100, 255))
                    screen.blit(loseText, (5, 240))
                    pygame.display.flip()
                    while enter:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                running=False
                                enter = False
                                break

                            if event.type == pygame.KEYDOWN:    #Vorbereitung auf neue runde
                                if event.key == pygame.K_RETURN:
                                    running = True
                                    enemies.clear()
                                    enemies = [Figurines.Enemy(random.randrange(0,440,5), random.randrange(0,20)), Figurines.Enemy(random.randrange(0,440,5), random.randrange(0,20))]
                                    selectedEnemy = enemies[1]
                                    flyingShot = 0
                                    score=0
                                    bullets.clear()
                                    enter = False
                                    break

                    clock.tick(60)
            if enter==False:
                break

        pygame.draw.rect(screen, (40, 100, 255), (0, 0, 480, 20))
        words=font.render(newWord,False,120,(40,100,255))       #scoreboard, input, output rendern
        scorerender=font.render(str(score),False,120,(40,100,255))
        inputrender=font.render(inputbox, False,120,(40,100,255))
        liverender=font.render(str(healthpoints), False,120,(40,100,255))
        Figurines.draw(screen,0,0,words)
        Figurines.draw(screen,0,462,scorerender)
        Figurines.draw(screen,460,0, liverender)
        Figurines.draw(screen,0,20,inputrender)

        for event in pygame.event.get(): #Event abfrage,

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                        pygame.event.post(pygame.event.Event(pygame.QUIT))

                elif event.key == pygame.K_BACKSPACE and len(inputbox)!=0:

                    inputbox = inputbox[0:-1]

                else:
                    inputbox += event.unicode

        if inputbox == newWord:
            if flyingShot != 1 and player.xPos == selectedEnemy.xPos:
                bullets.append(Figurines.Boolet(player.xPos, player.yPos))
                flyingShot = 1
                newWord = (giveWord(random.randrange(0, 370100)))
                inputbox=""

        pygame.display.flip()


game()
#Sountrack made by frostfire64#2701 on the best discord server
#https://github.com/dwyl/english-words --> Wörterbuch
#der https://www.pixilart.com/8-bit-adventure/gallery Artist für background, Schiffe und animationen eigenproduktion
#https://www.reddit.com/r/PixelArt/comments/bcvvd1/oc_space_time/ direkter link für background
#Font in Font ordner mit credit datei
#SPGLOBAL INC.