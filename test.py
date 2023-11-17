import sys, pygame
pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
position=[20,20]
white=[255,255,255]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                position[0]+=20


    screen.fill(white)
    pygame.draw.circle(screen,[255,0,0],position,5,5)
    pygame.display.flip()

pygame.quit()