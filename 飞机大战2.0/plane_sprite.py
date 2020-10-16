import random
import pygame

SCREEN_RECT = pygame.Rect(0,0,480,700)
CLOCK_NUM = 60
CREATE_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_name,speed=1):
        super().__init__()
        # self.image负责显示什么图片
        self.image = pygame.image.load(image_name)
        #self.image.get_rect()返回pygame.Rect(0,0,width,heigth)
        self.rect = self.image.get_rect()
        #self.rect负责在哪里显示
        self.speed = speed
    def update(self):
        self.rect.y += self.speed

class Background(GameSprite):
    #1.
    def __init__(self,is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.rect.y = -self.rect.height

class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")
        self.rect.bottom = 0
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
        self.speed = random.randint(1,3)

    def update(self):
        super().update()
        if self.rect.y == SCREEN_RECT.height:
            print("敌机飞出屏幕")
            self.kill()
    def __del__(self):
        print("飞出屏幕 %s" % self.rect)

class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/life.png",0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed
        if self.rect.x < 0 :
            self.rect.x = 0
        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
    def fire(self):
        #一次发送三颗子弹
        for i in (0,1,2):
            #生成子弹对象
            bullet = Bullet()
            bullet.rect.centerx = self.rect.centerx
            #每次子弹的bottom都不同，导致连续发送三颗子弹
            bullet.rect.bottom = self.rect.y - i * 20
            #添加到精灵组
            self.bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        super().__init__("./images/bullet1.png",-2)
        # self.rect.centerx =
    def update(self):
        super().update()

        #飞出游戏界面后销毁子弹
        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        print("tututu死掉")