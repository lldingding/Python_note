from plane_sprite import *
import pygame
pygame.init()
screen = pygame.display.set_mode((400,700))
bg = pygame.image.load("./images/background.png")
screen.blit(bg,(0,0))
pygame.display.update()

hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(150,300))
pygame.display.update()

clock = pygame.time.Clock()

hero_rect = pygame.Rect(150,300,102,126)

#生成对象敌机
enemy = GameSprite("./images/enemy1.png")
enemy1 = GameSprite("./images/enemy1.png",2)
#精灵加入精灵组
enemy_group = pygame.sprite.Group(enemy,enemy1)
#
while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("退出游戏")
            pygame.quit()
            exit()
    if hero_rect.y <= -126:
        hero_rect = 700

    screen.blit(bg,(0,0))
    screen.blit(hero,hero_rect)

    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()

pygame.quit()