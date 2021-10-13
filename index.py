import os
import pygame 
import pygame_menu
from pygame import mixer
from pygame.locals import *
import sys 


# Initialization

pygame.mixer.init()
pygame.init() 


 
# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'
 
# Game Resolution
width=800
height=600
screen=pygame.display.set_mode((width, height))



textbox = pygame.image.load('assets/images/textbox.png')
 
# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
 
    return newText
 
 
# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)
AMP_PINK=(242, 145, 233)
 
# Game Fonts
hamberger = "./assets/fonts/hamberger.ttf"
 
 
# Sounds
menukeys = mixer.Sound("assets\sounds\keypress.wav")


mixer.music.load("assets\sounds\strolling.wav")
mixer.music.play(-1)


# Game Framerate
clock = pygame.time.Clock()
FPS=60







def game():
    global textbox
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        screen.fill(black)
        screen.blit(textbox, (10,10))
        pygame.display.update()
        




def black_screen():
    global width, height
    i = 0
    while i == 0:
        blacc = pygame.Surface((width,height))
        blacc.fill((0,0,0))
        pygame.display.update()
        pygame.time.delay(2)
        i+=1
    game()


def fade(): 
    global width, height
    fade = pygame.Surface((width,height))
    fade.fill((0,0,0))
    for alpha in range(0, 300):
        fade.set_alpha(alpha)
        screen.blit(fade, (0,0))
        pygame.display.update()
        pygame.time.delay(6)
    black_screen()


# Main Menu
def main_menu():
 
    menu=True
    selected="start"
 
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    mixer.Sound.play(menukeys)
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    mixer.Sound.play(menukeys)
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    #Starts the game
                    mixer.Sound.play(menukeys)
                    if selected=="start":
                        fade()
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        screen.fill(AMP_PINK)
        title=text_format("SNATCHED", hamberger, 90, black)
        if selected=="start":
            text_start=text_format("START", hamberger, 75, white)
        else:
            text_start = text_format("START", hamberger, 75, black)
        if selected=="quit":
            text_quit=text_format("QUIT", hamberger, 75, white)
        else:
            text_quit = text_format("QUIT", hamberger, 75, black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        screen.blit(title, (width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Snatched - Main Menu")


#Initialize the Game
main_menu()
pygame.quit()
quit()



