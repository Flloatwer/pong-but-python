# pong by flloatwer. yes i know the ball is supposed to bounce in specific directions after hitting the paddle. yes i know the sound is scuffed. enjoy
import pygame
import sys
import numpy as np

pygame.init()

# create window
screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)

clock = pygame.time.Clock()
running = True

# sound stuff (copied from chatgpt because pysine wont install on my pc and i dont know how sound works in pygame)
pygame.mixer.init(frequency=44100,size=-16,channels=2)
def play(freq,dura):
 t=np.linspace(0,dura,int(44100*dura),False)
 s=(np.sin(2*np.pi*freq*t)*32767).astype(np.int16)
 s=np.column_stack([s,s])
 pygame.sndarray.make_sound(s).play()

# simple operations
def draw_paddle(x, y):
    pygame.draw.rect(screen, (0, 255, 0), (x, y, 10, 170))
def draw_ball(x, y):
    pygame.draw.rect(screen, (255, 0, 0,), (x, y, 15, 15))

# init some values
paddle1y = 200
paddle2y = 200
ballx = 100
bally = 200
balldx = 0
balldy = 0
ballspeed = 5
score1 = 0
score2 = 0

while running:
    # get window size
    width, height = screen.get_size()
    # exit check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # move paddles based on input
    keys = pygame.key.get_pressed()
    if paddle1y > 0:
        if keys[pygame.K_w]:
            paddle1y -= 7
    if paddle1y < height - 170:
        if keys[pygame.K_s]:
            paddle1y += 7
    if paddle2y > 0:
        if keys[pygame.K_o]:
            paddle2y -= 7
    if paddle2y < height - 170:
        if keys[pygame.K_l]:
            paddle2y += 7

    # check if ball is out of bounds and change direction if so
    if ballx <= 0:
        balldx = 0
        play(440, 0.2)
    elif ballx >= width - 15:
        balldx = 1
        play(400, 0.2)
    if bally <= 0: 
        balldy = 0
        play(400, 0.2)
    elif bally >= height - 15: 
        balldy = 1
        play(400, 0.2)
    
    # move and draw ball and also change its speed
    if keys[pygame.K_n]: 
        if ballspeed > 1: ballspeed -= 1
    if keys[pygame.K_m]: ballspeed += 1
    if balldx == 0:
        ballx += ballspeed
    else:
        ballx -= ballspeed
    if balldy == 0:
        bally += ballspeed
    else:
        bally -= ballspeed
    draw_ball(ballx, bally)

    # draw paddles
    draw_paddle(width - 10, paddle2y)
    draw_paddle(0, paddle1y)

    # check score
    if ballx == 0:
        if not (bally >= paddle1y and bally <= paddle1y + 170): 
            score2 += 1
            play(700, 0.2)
    if ballx == width - 15:
        if not (bally >= paddle2y and bally <= paddle2y + 170): 
            score1 += 1
            play(700, 0.2)
    caption = "Pong by Flloatwer - Left: " + str(score1) + " Right: " + str(score2)
    pygame.display.set_caption(caption)
    if score1 >= 10: 
        pygame.display.set_caption("Pong by Flloatwer - LEFT WON!!!")
        play(200, 0.001)
    if score2 >= 10: 
        pygame.display.set_caption("Pong by Flloatwer - RIGHT WON!!!")
        play(200, 0.001)

    # print debug values
    print(score1, score2, paddle1y, paddle2y, width, height, ballx, bally, balldx, balldy)
    # update screen
    pygame.display.flip() 
    screen.fill((0, 0, 0)) 
    clock.tick(60) 

pygame.quit()
sys.exit()
