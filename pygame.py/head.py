import pygame
pygame.init()
screen=pygame.display.set_mode([1000, 500])
pygame.display.set_caption("Progect with")
while True:
    screen.fill([255, 255, 255])
    events=pygame.event.get()
    # creating themes
    
    for event in events:
        if event.type==pygame.QUIT:
            exit()

    pygame.display.update()