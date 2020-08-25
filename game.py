# 1 - Import library
import pygame
from pygame.locals import *
import math
import random

# 2 - Initialize game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
keys = [False, False, False, False, False]
playerpos=[100,100] # width, height

acc =[0,0]
arrows=[]
arrow = pygame.image.load("C:/Users/Penguin/Desktop/penguin_game/Ninja_Star_Pixel.png") #gotta find image some other time
arrow = pygame.transform.scale(arrow, (50,50))

badtimer = 100
badtimer1 = 0
badguys= [[640,100]]
healthvalue = 194

pygame.mixer.init()

# 3 - Load imgs
player = pygame.image.load("C:/Users/Penguin/Desktop/penguin_game/penguin.png")
player = pygame.transform.scale(player, (100,100))
background = pygame.image.load("C:/Users/Penguin/Desktop/penguin_game/pepe2.jpg")

castle = pygame.image.load("C:/Users/Penguin/Desktop/penguin_game/gigachad.png")
castle = pygame.transform.scale(castle, (100,100))

badguyimg1 = pygame.image.load("C:/Users/Penguin/Desktop/penguin_game/Ricardo_Milos_transparent.png")
badguyimg1 = pygame.transform.scale(badguyimg1, (80,80))
badguyimg = badguyimg1

healthbar = pygame.image.load("C:/Users/Penguin/Desktop/penguin_game/healthbar.png")
healthbar = pygame.transform.scale(healthbar, (255,32))
health = pygame.image.load("C:/Users/Penguin/Desktop/penguin_game/health.png")
health = pygame.transform.scale(health, (10,18))

gameover = pygame.image.load("C:/Users/Penguin/Desktop/penguin_game/omae.png")
youwin = pygame.image.load("C:/Users/Penguin/Desktop/penguin_game/win.jpg")

# 3.1 - Load audio
hit = pygame.mixer.Sound("C:/Users/Penguin/Desktop/penguin_game/EXPLODE.wav")
enemy = pygame.mixer.Sound("C:/Users/Penguin/Desktop/penguin_game/enemy.ogg")
shoot = pygame.mixer.Sound("C:/Users/Penguin/Desktop/penguin_game/shoot.ogg")
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)
pygame.mixer.music.load("C:/Users/Penguin/Desktop/penguin_game/Mass_Destruction.wav")
pygame.mixer.music.play(-1,0.0)
pygame.mixer.music.set_volume(0.25)

# 4 - keep looping through
running = 1
exitcode = 0
while running:
    badtimer -= 1
    # 5 - clear the screen before drawing again
    screen.fill(0)
    # 6 - draw screen elements
    screen.blit(background,(-260,-280))
    screen.blit(castle,(0,30))
    screen.blit(castle,(0,135))
    screen.blit(castle,(0,240))
    screen.blit(castle,(0,345))

    # 6.1 - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1]-(playerpos[1]+30),position[0]-(playerpos[0]+26))
    playerrot = pygame.transform.rotate(player, 360-angle*57.29)
    playerpos1 = (playerpos[0]-playerrot.get_rect().width/2, playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot, playerpos1)

    # 6.2 - Draw arrows
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0])*10
        vely = math.sin(bullet[0])*10
        bullet[1]+=velx
        bullet[2]+=vely
        if bullet[1] <- 64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(arrow, 360-projectile[0]*57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # 6.3 - Draw bad guys
    if badtimer == 0:
        badguys.append([640, random.randint(50,430)])
        badtimer = 100 - (badtimer1*2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index = 0
    for badguy in badguys:
        if badguy[0] <- 64:
            badguys.pop(index)
        badguy[0] -= 7
        # 6.3.1 - Attack castle 
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            hit.play()
            healthvalue -= random.randint(5,20)
            badguys.pop(index)
        # 6.3.2 - Check for collisions
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(arrow.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                enemy.play()
                acc[0] += 1
                badguys.pop(index)
                arrows.pop(index1)
            index1 += 1
        index += 1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)

    # 6.4 - Draw clock
    #font = pygame.font.Font(None, 10)
    #survivedtext = font.render(str((90000 - pygame.time.get_ticks())/60000)+ ":" + str((90000 - pygame.time.get_ticks())/1000%60).zfill(2), True, (0,0,0))
    #textRect = survivedtext.get_rect()
    #textRect.topright = [635,5]
    #screen.blit(survivedtext, textRect)

    # 6.5 - Draw health bar
    screen.blit(healthbar, (5,5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1+53,12))

    # 7 - update screen
    pygame.display.flip()
    # 8 - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        # add ons here
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                #print('left')
                keys[0]=True
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                #print('right')
                keys[1]=True
            if event.key == pygame.K_UP or event.key == ord('w'):
                #print('up')
                keys[2]=True
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                #print('down')
                keys[3]=True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                #print('left stop')
                keys[0]=False
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                #print('right stop')
                keys[1]=False
            if event.key == pygame.K_UP or event.key == ord('w'):
                #print('up stop')
                keys[2]=False
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                #print('down stop')
                keys[3]=False
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            shoot.play()
            position = pygame.mouse.get_pos()
            acc[1]+=1
            arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])

    # 9 - Move player
    if keys[0]:
        playerpos[0] -= 5
    elif keys[2]:
        playerpos[1] -= 5
    if keys[1]:
        playerpos[0] += 5
    elif keys[3]:
        playerpos[1] += 5

    # 10 - Win/Lose check
    #if pygame.time.get_ticks() >= 90000:
    #    running = 0
    #    exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    if acc[1] != 0:
        accuracy = acc[0] * 1.0 / acc[1] * 100
    else:
        accuracy = 0

# 11 - Win/lose display
if exitcode == 0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery
    screen.blit(gameover, (0,0))
    screen.blit(text, textRect)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: " + str(accuracy) + "%", True, (255,0,0))
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()
    
        





        
