#-------------------------------------------------------
#-------------------- Snake Game -----------------------
#-------------------------------------------------------

import pygame
import sys
import random

# important variables

pygame.init()
game_running = False
clock = pygame.time.Clock()
game_title = pygame.display.set_caption("Snake")
icon = pygame.image.load(r"snake_start_screen.png")
if icon is None :
    raise Exception("Unable to load icon")
else :
    pygame.display.set_icon(icon)

# font

font = pygame.font.Font(r"Pixeltype.ttf" , 50)
if font is None :
    raise Exception("Unable to load text")

# screen

width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# game colors

dark_green = (0,100,0)
red = (255,0,0)

# start screen

snake_image = pygame.transform.scale(pygame.image.load(r"original-sin.png"), (200, 200))
if snake_image is None :
    raise Exception("Unable to load image")
snake_image_rect = snake_image.get_rect(center = (400, 300))

title = font.render("Snake Game", False, "Gold")
title_rect = title.get_rect(center = (400, 100))

button_width = 200
button_height = 50
button_x = (width - button_width) // 2
button_y = (height - button_height) - 50

def draw_button(text, x, y, width, height, normal_color, hover_color):
    global game_running, score

    mouse_pos = pygame.mouse.get_pos()

    button_rect = pygame.Rect(x, y, width, height)
    color = hover_color if button_rect.collidepoint(mouse_pos) else normal_color

    pygame.draw.rect(screen, color, button_rect)
    pygame.draw.rect(screen, "Black", button_rect, 2)

    text_surf = font.render(text, True, "Black")
    text_rect = text_surf.get_rect(center = button_rect.center)
    screen.blit(text_surf, text_rect)

    if text_rect.collidepoint(mouse_pos) :
        if pygame.mouse.get_pressed()[0] :
            game_running = True
            score = 0
            return game_running

# Snake

snake_x, snake_y = 400, 300
pos_x, pos_y = 10, 0
snake_body = [(snake_x, snake_y)]

apple_x, apple_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10

score = 0
game_over = False
previous_score = 0
highest_score = 0
def snake() :

    global snake_x, snake_y, apple_x, apple_y, snake_body, game_running, score, pos_x, pos_y, game_over, previous_score, highest_score

    snake_x = (snake_x + pos_x)%width
    snake_y = (snake_y + pos_y)%height

    if (snake_x, snake_y) in snake_body :
        game_running = False
        game_over = True
        snake_body = [(snake_x, snake_y)]
        snake_x, snake_y = 400, 300
        pos_x = 10
        pos_y = 0

    snake_body.append((snake_x, snake_y))

    if apple_x == snake_x and apple_y == snake_y :
        score += 1
        while (apple_x, apple_y) in snake_body :
            apple_x, apple_y = random.randrange(0, width)//10*10, random.randrange(0, height)//10*10
    else :
        del snake_body[0]

    pygame.draw.rect(screen, red, [apple_x, apple_y, 10, 10])
    for (i, j) in snake_body :
        pygame.draw.rect(screen, dark_green, [i, j, 10, 10])

    previous_score = score
    if score > highest_score :
        highest_score = score

# score

def game_score() :

    score_1 = font.render(f"Your score is : {previous_score} ", False, "Gold")
    score_1_rect = score_1.get_rect(center = (400, 300))

    score_2 = font.render(f"Highest score : {highest_score} ", False, "Gold")
    score_2_rect = score_2.get_rect(center = (400, 200))

    screen.blit(score_1, score_1_rect)
    screen.blit(score_2, score_2_rect)


# ------------ main loop ------------

while True :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN :

            if event.key == pygame.K_w or event.key == pygame.K_UP :
                if pos_y != 10 :
                    pos_x = 0
                    pos_y = -10

            if event.key == pygame.K_a or event.key == pygame.K_LEFT :
                if pos_x != 10 :
                    pos_x = -10
                    pos_y = 0

            if event.key == pygame.K_s or event.key == pygame.K_DOWN :
                if pos_y != -10 :
                    pos_x = 0
                    pos_y = 10

            if event.key == pygame.K_d or event.key == pygame.K_RIGHT :
                if pos_x != -10 :
                    pos_x = 10
                    pos_y = 0

    screen.fill("Black")

    if game_running :

        snake()

        score

    else :
        if game_over:

            draw_button("Play",button_x,button_y,button_width,button_height,"Gold", "White")
            game_score()

        else :

            screen.blit(snake_image, snake_image_rect)
            screen.blit(title, title_rect)
            draw_button("Play",button_x,button_y,button_width,button_height,"Gold", "White")

    pygame.display.update()
    clock.tick(13)
