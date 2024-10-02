import pygame, random 
from pygame.locals import *
pygame.init()


def on_grid_random():
    x = random.randint(0,690)
    y = random.randint(0,690)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

screen =pygame.display.set_mode((700,700))
pygame.display.set_caption('snake')

snake=[(200,200),(210,200), (220,200)]
snake_skin=pygame.Surface((10,10))
snake_skin.fill((0,255,0))

apple_pos=(random.randint(0,690)),random.randint(0,690)
apple =pygame.Surface((10,10))
apple.fill((255,0,0))
my_direction = K_LEFT

clock=pygame.time.Clock()


while True:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type ==quit:
                pygame.quit()
                
            if event.type ==KEYDOWN:
                if event.key==K_UP:
                    my_direction = UP # type: ignore
                if event.key==K_DOWN:
                    my_direction = DOWN # type: ignore
                if event.key==K_LEFT:
                    my_direction = LEFT 
                if event.key==K_RIGHT:
                    my_direction = RIGHT 
        
        if my_direction== UP:
            snake[0]=(snake[0][0], snake[0][1]-10)
        if my_direction==DOWN:
            snake[0]=(snake[0][0], snake[0][1]+10)   
        if my_direction==K_RIGHT:
            snake[0]=(snake[0][0] + 10, snake[0][1]) 
        if my_direction==K_LEFT:
            snake[0]=(snake[0][0] - 10, snake[0][1])    
            
        for i in range(len(snake) - 1, 0 ,-1):
            snake[i] = (snake[i-1][0], snake[i-1][1])
             
        screen.fill((0,0,0))
        screen.blit(apple, apple_pos)
        for pos in snake:
            screen.blit(snake_skin,pos)
            
        pygame.display.update()
