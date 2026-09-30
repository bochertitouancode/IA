import pygame

pygame.init()
screen = pygame.display.set_mode((1024, 576))
clock = pygame.time.Clock()
run = True

while run:

    pygame.display.flip()
    if pygame.key.get_pressed() == pygame.K_ESCAPE:
                print("kk")
                run = False
                pygame.quit()


    for event in pygame.event.get():
        
        if event.type == pygame.quit:
            run = False
            pygame.quit()

    clock.tick(120)