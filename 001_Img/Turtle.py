import pygame
 
# pyGameの初期化
pygame.init()
# Windowの作成 (640px x 480px)の大きさ 
screen = pygame.display.set_mode((640, 480))
 
# イメージを用意
TurtleImg = pygame.image.load("Turtle.png").convert_alpha()
 
done = False
clock = pygame.time.Clock()

# doneがFalseの間はずっとループ
while not done:
    # 終了処理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # 今回のお題
    screen.fill((255, 255, 255))
    screen.blit(TurtleImg, (10,10)) 
    pygame.display.flip()
    clock.tick(60)
    