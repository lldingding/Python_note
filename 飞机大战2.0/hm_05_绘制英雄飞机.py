import pygame

pygame.init()
screen = pygame.display.set_mode((480,700))
#在主窗口绘制背景图片
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()
#在主窗口绘制英雄飞机图片
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(200,500))
pygame.display.update()

while True:
    pass
#此处报错是因为while不断循环，到不了quit，不需要理会
pygame.quit()