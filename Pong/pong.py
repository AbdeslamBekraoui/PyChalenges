# ----------------------
# -------- Pong --------
# ----------------------

import pygame
import sys
import random

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font("Pixeltype.ttf", 50)
sound = pygame.mixer.Sound("269718__michorvath__ping-pong-ball-hit.wav")

# screen

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# caption and icon

pygame.display.set_caption("Pong")

icon = pygame.image.load("ping-pong.png").convert_alpha()
if icon is None :
    raise Exception("Unable to load image!")
else :
    pygame.display.set_icon(icon)

# game variables

ball = pygame.Rect(width/2 - 7.5, height/2 - 7.5, 15, 15)
speed_x = 7
speed_y = 7
raquette = pygame.Rect(width - 50, height/2, 15, 100)
bot = pygame.Rect(50, height/2, 15, 100)
bot_score = 0
player_score =0

def ball_movement() :
    global speed_x, speed_y, player_score, bot_score

    ball.x += speed_x
    ball.y += speed_y

    if ball.bottom >= height or ball.top <= 0 :
        sound.play()
        speed_y *= -1

    if ball.right >=  width :
        ball.x = width/2 -7.5
        bot_score += 1

    if ball.left <= 0 :
        ball.x = width/2 -7.5
        player_score += 1

    if ball.colliderect(raquette) or ball.colliderect(bot):
        sound.play()
        speed_x *= -1

# -------------- Main loop --------------

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()

    pygame.mouse.set_visible(False)
    screen.fill("Black")

    # game controler

    mouse = pygame.mouse.get_pos()
    if mouse[1] != 0  :
        raquette.y = mouse[1]
    if raquette.bottom >= 600 :
        raquette.bottom = 600

    ball_movement()

    if player_score == 10 or bot_score == 10 :
        player_score = 0
        bot_score = 0

    # score

    score_1 = font.render(f"{bot_score}", False, "White")
    score_1_rect = score_1.get_rect(center = (350, 20))
    score_2 = font.render(f"{player_score}", False, "White")
    score_2_rect = score_1.get_rect(center = (450, 20))
    screen.blit(score_1, score_1_rect)
    screen.blit(score_2, score_2_rect)

    # bot movement

    if bot.top < ball.y :
        bot.top += 15
    if bot.bottom > ball.y :
        bot.bottom -= 15

    # game objects

    pygame.draw.rect(screen, "White", ball)
    pygame.draw.rect(screen, "White", raquette)
    pygame.draw.rect(screen, "White", bot)
    pygame.draw.rect(screen, "White", [width/2 - 7.5, 0, 15, 800])

    pygame.display.flip()
    clock.tick(60)
