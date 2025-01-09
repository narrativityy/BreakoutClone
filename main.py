import pygame

# initialization
pygame.init()
screen = pygame.display.set_mode((800, 600), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
running = True

# paddle attributes
paddle_width = 200
paddle_height = 20
paddle_left = screen.get_width() / 2 - paddle_width / 2
paddle_top = screen.get_height() - paddle_height - 20
paddle_speed = 800

# game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # background
    screen.fill('black')

    # main logic

    # drawing paddle
    pygame.draw.rect(screen, 'white', (paddle_left, paddle_top, paddle_width, paddle_height), 0, 10)

    # getting user input
    keys = pygame.key.get_pressed()

    # paddle movement
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        paddle_left -= paddle_speed * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        paddle_left += paddle_speed * dt

    # resetting frame
    pygame.display.flip()

    # setting fps and delta time
    dt = clock.tick(60) / 1000

pygame.quit()