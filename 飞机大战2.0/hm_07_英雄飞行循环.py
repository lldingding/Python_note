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
#保存英雄位置
hero_rect =  pygame.Rect(200,500,102,126)
#对象clock
clock = pygame.time.Clock()
while True:
    clock.tick(1)
    #可以在此放置监听
    #xxxxxxxxxxxx
    hero_rect.y -= 50
    #循环飞行
    if hero_rect.y <= -126:
        hero_rect.y = 700
    #加入背景图片循环，否则飞机会出现重叠部分
    screen.blit(bg, (0, 0))
    #
    screen.blit(hero, hero_rect)
    pygame.display.update()
#此处报错是因为while不断循环，到不了quit，不需要理会
pygame.quit()