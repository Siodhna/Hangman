import pygame

pygame.init()

Screen = pygame.display.set_mode((win_width, win_height))  # teeb akna
pygame.display.set_caption("Hangman")  # aknale pealkiri



gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONUP:



    pygame.display.update()

    pygame.quit()
    quit()

