import pygame
pygame.init()
screen = pygame.display.set_mode((480,700))
while True:
    even_list = pygame.event.get()
    for event in even_list:
        if event.type == pygame.QUIT:
            print("out out out !!!")
            pygame.quit()
            exit()


pygame.quit()