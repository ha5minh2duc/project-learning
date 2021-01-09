# Project: CAR RACING GAME
# Name   : Ha Minh Duc
# ID     : 11191084

# Description: Player has to use 4 buttons (left, right, up, down) to control the car to avoid obstacles on the road

import pygame, sys
from pygame import mixer
import time
import random

pygame.init()  # khởi tạo môi trường

gray  = (119, 118, 110)
black = (0, 0, 0)
red   = (255, 0, 0)
green = (0, 200, 0)
blue  = (0, 0, 200)
bright_red   = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue  = (0, 0, 255)
display_width  = 800
display_height = 600

# Set up screen & needed images
gamedisplays = pygame.display.set_mode((display_width, display_height))   # tạo của sổ trò chơi (chiều dài, chiều cao)
pygame.display.set_caption("CAR GAME")   # Tạo tiêu đề game trên main tab --> CAR GAME
clock = pygame.time.Clock()

carimg                 = pygame.image.load(r'C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\car1.jpg')
backgroundpic          = pygame.image.load(r'C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\grass.jpg')
yellow_strip           = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\yellow_strip.jpg")
strip                  = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\strip.jpg")
intro_background       = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\ground.jpg")
instruction_background = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\ground2.jpg")
car_width = 56
pause = False


def text_objects(text, font):
    textsurface = font.render(text, True, black)  # draw text on a Surface
    return textsurface, textsurface.get_rect()  # get_rect method: creates a new rect with the size of the image & the x,y coordinates (0,0)


def intro_loop():
    # cửa sổ cần phải hiển thị cho đến khi ta click vào nút (x) để đóng nó một cách tường minh
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.blit(intro_background, (0, 0))    # blit --> vẽ intro_background ở góc trái screen(tọa độ (0,0)
        largetext = pygame.font.Font('freesansbold.ttf', 115)  # lựa chọn font chữ
        TextSurf, TextRect = text_objects("CAR GAME", largetext)
        TextRect.center = (400, 100)    # Căn chỉnh hình chữ nhật theo tọa độ
        gamedisplays.blit(TextSurf, TextRect)

        button("START", 150, 520, 100, 50, green, bright_green, "play")
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")
        button("INSTRUCTION", 300, 520, 200, 50, blue, bright_blue, "intro")

        pygame.display.update()   # update() giúp cập nhật mọi thay đổi trên cửa sổ
        clock.tick(50)  #update the clock (This method should be called once per frame & how many milliseconds have passed since the previous call)


def button(message, x, y, w, h, color, bright_color, action=None):
    # Mouse moving
    mouse = pygame.mouse.get_pos()       # get_pos() --> xác định vị trí của con trỏ chuột (get the state of the mouse buttons)
    click = pygame.mouse.get_pressed()   # get_pressed() --> click vào 1 vị trí nào đó trong cửa sổ (get the mouse cursor position)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, color, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "menu":
                intro_loop()
            elif action == "pause":
                paused()
            elif action == "unpause":
                mixer.music.unpause()
                unpaused()

    else:
        pygame.draw.rect(gamedisplays, bright_color, (x, y, w, h))

    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textsurf, textrect = text_objects(message, smalltext)
    textrect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplays.blit(textsurf, textrect)


def introduction():
    # cửa sổ cần phải hiển thị cho đến khi ta click vào nút (x) để đóng nó một cách tường minh
    introduction = True

    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.blit(instruction_background, (0, 0))
        largetext  = pygame.font.Font('freesansbold.ttf', 80)
        smalltext  = pygame.font.Font('freesansbold.ttf', 20)
        mediumtext = pygame.font.Font('freesansbold.ttf', 40)

        textSurf, textRect = text_objects("This is an car game in which you need dodge the coming cars", smalltext)
        textRect.center = ((350), (200))
        TextSurf, TextRect = text_objects("INSTRUCTION", largetext)
        TextRect.center = ((400), (100))
        gamedisplays.blit(TextSurf, TextRect)
        gamedisplays.blit(textSurf, textRect)
        stextSurf, stextRect = text_objects("ARROW LEFT : LEFT TURN", smalltext)
        stextRect.center = ((150), (400))
        hTextSurf, hTextRect = text_objects("ARROW RIGHT : RIGHT TURN", smalltext)
        hTextRect.center = ((150), (450))
        sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext)
        sTextRect.center = ((350), (300))
        gamedisplays.blit(sTextSurf, sTextRect)
        gamedisplays.blit(stextSurf, stextRect)
        gamedisplays.blit(hTextSurf, hTextRect)

        button("BACK", 600, 450, 100, 50, blue, bright_blue, "menu")

        pygame.display.update()
        clock.tick(30)

def background():
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(backgroundpic, (0, 200))
    gamedisplays.blit(backgroundpic, (0, 400))
    gamedisplays.blit(backgroundpic, (700, 0))
    gamedisplays.blit(backgroundpic, (700, 200))
    gamedisplays.blit(backgroundpic, (700, 400))
    gamedisplays.blit(yellow_strip, (400, 0))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 200))
    gamedisplays.blit(yellow_strip, (400, 300))
    gamedisplays.blit(yellow_strip, (400, 400))
    gamedisplays.blit(yellow_strip, (400, 500))
    gamedisplays.blit(strip, (120, 0))
    gamedisplays.blit(strip, (120, 100))
    gamedisplays.blit(strip, (120, 200))
    gamedisplays.blit(strip, (680, 0))
    gamedisplays.blit(strip, (680, 100))
    gamedisplays.blit(strip, (680, 200))


def countdown_background():
    font = pygame.font.SysFont(None, 25)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    gamedisplays.blit(backgroundpic, (0, 0))
    gamedisplays.blit(backgroundpic, (0, 200))
    gamedisplays.blit(backgroundpic, (0, 400))
    gamedisplays.blit(backgroundpic, (700, 0))
    gamedisplays.blit(backgroundpic, (700, 200))
    gamedisplays.blit(backgroundpic, (700, 400))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 200))
    gamedisplays.blit(yellow_strip, (400, 300))
    gamedisplays.blit(yellow_strip, (400, 400))
    gamedisplays.blit(yellow_strip, (400, 100))
    gamedisplays.blit(yellow_strip, (400, 500))
    gamedisplays.blit(yellow_strip, (400, 0))
    gamedisplays.blit(yellow_strip, (400, 600))
    gamedisplays.blit(strip, (120, 200))
    gamedisplays.blit(strip, (120, 0))
    gamedisplays.blit(strip, (120, 100))
    gamedisplays.blit(strip, (680, 100))
    gamedisplays.blit(strip, (680, 0))
    gamedisplays.blit(strip, (680, 200))
    gamedisplays.blit(carimg, (x, y))
    text = font.render("PASSED: 0", True, black)
    score = font.render("SCORE: 0", True, red)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))
    button("PAUSE", 650, 0, 150, 50, blue, bright_blue, "pause")


def countdown():
    countdown = True

    while countdown:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("3", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)

        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("2", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)

        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("1", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)

        gamedisplays.fill(gray)
        countdown_background()
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("GO!!!", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(1)

        game_loop()


def paused():
    global pause

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("PAUSED", largetext)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(TextSurf, TextRect)

        mixer.music.pause()

        button("CONTINUE", 150, 450, 150, 50, green, bright_green, "unpause")
        button("RESTART", 350, 450, 150, 50, blue, bright_blue, "play")
        button("MAIN MENU", 550, 450, 200, 50, red, bright_red, "menu")

        pygame.display.update()
        clock.tick(30)


def unpaused():
    global pause
    pause = False


def obstacle(obs_startx, obs_starty, obs):
    if obs == 0:
        obs_pic = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\car1.jpg")
    elif obs == 1:
        obs_pic = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\car2.jpg")
    elif obs == 2:
        obs_pic = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\car2.jpg")
    elif obs == 3:
        obs_pic = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\car4.jpg")
    elif obs == 4:
        obs_pic = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\car5.jpg")
    elif obs == 5:
        obs_pic = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\car6.jpg")
    elif obs == 6:
        obs_pic = pygame.image.load(r"C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\car7.jpg")
    gamedisplays.blit(obs_pic, (obs_startx, obs_starty))



def score_system(passed, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("PASSED: " + str(passed), True, black)
    score = font.render("SCORE: " + str(score), True, red)
    gamedisplays.blit(text, (0, 50))
    gamedisplays.blit(score, (0, 30))


def message_display(text):
        largetext = pygame.font.Font("freesansbold.ttf", 80)
        textsurf, textrect = text_objects(text, largetext)
        textrect.center = ((display_width / 2), (display_height / 2))
        gamedisplays.blit(textsurf, textrect)
        pygame.display.update()
        time.sleep(3)
        game_loop()

def crash():
    message_display("YOU CRASHED")


def car(x, y):
    gamedisplays.blit(carimg, (x, y))


def game_loop():
    # Music
    mixer.music.load(r'C:\\Users\Dell\Videos\New folder\Hà Minh Đức - Midterm\The Script - Hall Of Fame .mp3')
    mixer.music.play()

    global pause
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    obstacle_speed = 10
    obs = 0
    y_change = 0
    obs_startx = random.randrange(200, (display_width - 200))
    obs_starty = -750
    obs_width = 56
    obs_height = 125
    passed = 0
    level = 0
    score = 0
    y2 = 7
    fps = 120

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_a:
                    obstacle_speed += 3
                if event.key == pygame.K_b:
                    obstacle_speed -= 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        pause = True
        gamedisplays.fill(gray)

        rel_y = y2 % backgroundpic.get_rect().width
        gamedisplays.blit(backgroundpic, (0, rel_y - backgroundpic.get_rect().width))
        gamedisplays.blit(backgroundpic, (700, rel_y - backgroundpic.get_rect().width))
        if rel_y < 800:
            gamedisplays.blit(backgroundpic, (0, rel_y))
            gamedisplays.blit(backgroundpic, (700, rel_y))
            gamedisplays.blit(yellow_strip, (400, rel_y))
            gamedisplays.blit(yellow_strip, (400, rel_y + 100))
            gamedisplays.blit(yellow_strip, (400, rel_y + 200))
            gamedisplays.blit(yellow_strip, (400, rel_y + 300))
            gamedisplays.blit(yellow_strip, (400, rel_y + 400))
            gamedisplays.blit(yellow_strip, (400, rel_y + 500))
            gamedisplays.blit(yellow_strip, (400, rel_y - 100))
            gamedisplays.blit(strip, (120, rel_y - 200))
            gamedisplays.blit(strip, (120, rel_y + 20))
            gamedisplays.blit(strip, (120, rel_y + 30))
            gamedisplays.blit(strip, (680, rel_y - 100))
            gamedisplays.blit(strip, (680, rel_y + 20))
            gamedisplays.blit(strip, (680, rel_y + 30))

        y2 += obstacle_speed

        obs_starty -= (obstacle_speed / 4)
        obstacle(obs_startx, obs_starty, obs)
        obs_starty += obstacle_speed
        car(x, y)
        score_system(passed, score)
        if x > 690 - car_width or x < 110:
            crash()
        if x > display_width - (car_width + 110) or x < 110:
            crash()
        if obs_starty > display_height:
            obs_starty = 0 - obs_height
            obs_startx = random.randrange(170, (display_width - 170))
            obs = random.randrange(0, 7)
            passed = passed + 1
            score = passed * 3
            if int(passed) % 10 == 0:
                level += 1
                obstacle_speed += 2
                largetext = pygame.font.Font("freesansbold.ttf", 80)
                textsurf, textrect = text_objects("LEVEL " + str(level), largetext)
                textrect.center = ((display_width / 2), (display_height / 2))
                gamedisplays.blit(textsurf, textrect)
                pygame.display.update()
                time.sleep(3)

        if y < obs_starty + obs_height:
            if x > obs_startx and x < obs_startx + obs_width or x + car_width > obs_startx and x + car_width < obs_startx + obs_width:
                crash()

        button("Pause", 650, 0, 150, 50, blue, bright_blue, "pause")
        pygame.display.update()
        clock.tick(60)


intro_loop()
game_loop()
pygame.quit()
quit()
