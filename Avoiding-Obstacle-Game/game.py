import random
import pygame
import time

pygame.init()

windowWidth = 600
windowHeight = 700
playerWidth = 100
playerHeight = 103
Playerspeed = 6

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

playerImg = pygame.image.load('player.png')
gameDisplay = pygame.display.set_mode((windowWidth,windowHeight))
pygame.display.set_caption("A bit Racey")
clock = pygame.time.Clock()

def ThingsDaughed(score):
    font = pygame.font.Font(None,25)
    text = font.render("Score : "+str(score),True,black)
    gameDisplay.blit(text, (0,0))

def Things(Tx,Ty,TWidth,THeight,color):
    pygame.draw.rect(gameDisplay,color, [Tx,Ty,TWidth,THeight])

def TextObjects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()

def ShowMessage(text):
    font = pygame.font.Font('freesansbold.ttf',80)
    textSurface, textRect = TextObjects(text, font)
    textRect.center = ((windowWidth/2,windowHeight/2))
    gameDisplay.blit(textSurface,textRect)
    pygame.display.update()
    time.sleep(1.2)
    GameLoop()

def Crash():
    ShowMessage("You Crashed")

def Player(x,y):
    gameDisplay.blit(playerImg,(x,y))

def GameLoop():
    x = windowWidth/2 - playerWidth/2
    y = windowHeight -100

    xChange = 0
    Tx = [random.randrange(0,windowWidth-100)]
    Ty = [-600]
    TSpeed = 9
    TWidth = [100]
    THeight = [100]

    score = 0
    NoThings = 1
    counter = 4
    countDecission = 0

    exitGame = False
    while not exitGame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        xChange = Playerspeed
                    elif event.key == pygame.K_LEFT:
                        xChange = -Playerspeed

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0

        x += xChange

        gameDisplay.fill(white)
        for i in range(0, NoThings):
            Things(Tx[i],Ty[i],TWidth[i],THeight[i],black)
            if NoThings > countDecission:
                countDecission += 1
                Tx.append(random.randrange(0,windowWidth))
                Ty.append(-600)
                TWidth.append(random.randrange(0,100))
                THeight.append(random.randrange(0,100))


        Player(x,y)
        ThingsDaughed(score) #At last so nothing overlaps it

        if x > windowWidth-playerWidth or x < 0:
            Crash()
        # print(event)
        for i in range (0,NoThings):
            if Ty[i] > windowHeight:
                score += 1
                if score == counter:
                    NoThings += 1
                    counter += 15
                TSpeed += 0.16

                Ty[i] = 0 - playerWidth
                Tx[i] = random.randrange(0,windowWidth-100)
                TWidth[i] = random.randrange(50,110)
                THeight[i] = random.randrange(50,100)


        for i in range(0,NoThings):
            if y-2 <= Ty[i]+THeight[i]:
                if (x+playerWidth > Tx[i] and x < Tx[i]+TWidth[i]): #My logic isent it cool
                    Crash()

        for i in range(0,NoThings):
            Ty[i] += TSpeed
        clock.tick(100)
        pygame.display.update()
        # It updates a part
        # pygame.display.flip()
        # It updates the whole  screen


GameLoop()
pygame.quit()
quit()
