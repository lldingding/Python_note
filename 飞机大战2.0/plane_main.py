import pygame
from plane_sprite import *


class GamePlay(object):
    """创建游戏类"""
    def __init__(self):
    # 游戏初始化
        #1.创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        #2.创建时钟
        self.clock = pygame.time.Clock()
        #3.调用私有方法（创建精灵和精灵组）
        self.__create_sprite()
        #4.创建定时器
        pygame.time.set_timer(CREATE_ENEMY_EVENT,1000)

        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprite(self):
        #背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_ground = pygame.sprite.Group(bg1,bg2)
        #敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        #英雄精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
    # 开始游戏

        while True:
            # 1.设置刷新率
            self.clock.tick(CLOCK_NUM)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新绘制精灵组
            self.__update_sprite()
            #5.更新屏幕显示
            pygame.display.update()

    def __event_handler(self):
        """监听事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                GamePlay.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

        #按键捕获
        self.keys_pressed = pygame.key.get_pressed()
        if self.keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif self.keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -2
        else:
            self.hero.speed = 0

    def __check_collide(self):
        """碰撞检测"""
        #精灵组碰撞精灵组，返回字典【敌机碰撞子弹】
        pygame.sprite.groupcollide(self.enemy_group,self.hero.bullets,True,True)
        #精灵碰撞精灵组，返回元组【敌机碰撞英雄】
        sprite_list = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
        if len(sprite_list) > 0 :
            #英雄死去
            self.hero.kill()
            GamePlay.__game_over()


    def __update_sprite(self):
        #背景精灵组更新
        self.back_ground.update()
        self.back_ground.draw(self.screen)
        # 敌机精灵组更新
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        #英雄精灵组更新
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 子弹精灵组更新
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()

if __name__ == "__main__":
    # 创建游戏对象
    plane_demo = GamePlay()
    # 开始游戏
    plane_demo.start_game()