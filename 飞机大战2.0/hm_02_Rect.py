import pygame
#在调用Rect时，可以不调用方法init（）
pygame.init()
#Pygame内部有pygame.Rect()类（）内部、
hm_rect = pygame.Rect(10,30,100,160)
print("x和y %d %d" % (hm_rect.x,hm_rect.y))
#size方法返回元组
print("tuple %d %d" % hm_rect.size)

pygame.quit()