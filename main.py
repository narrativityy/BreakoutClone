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

# ball attributes
ball_x = screen.get_width() / 2
ball_y = screen.get_height() / 2
ball_radius = 20
ball_speed = 400
ball_x_direction = 1
ball_y_direction = 1

# game loop
while running:
    # setting fps and delta time
    dt = clock.tick(60) / 1000

    # handling events
    for event in pygame.event.get():
        # quit
        if event.type == pygame.QUIT:
            running = False

    # background
    screen.fill('black')

    # main logic

    # drawing paddle
    pygame.draw.rect(screen, 'red', (paddle_left, paddle_top, paddle_width, paddle_height), 0, 10)

    # drawing ball
    pygame.draw.circle(screen, 'white', (ball_x, ball_y), ball_radius)

    # getting user input
    keys = pygame.key.get_pressed()

    # paddle movement
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        # preventing paddle from going out of screen
        if paddle_left <= 0:
            paddle_left = 0
        else:
            paddle_left -= paddle_speed * dt
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        # preventing paddle from going out of screen
        if paddle_left >= screen.get_width() - paddle_width:
            paddle_left = screen.get_width() - paddle_width
        else:
            paddle_left += paddle_speed * dt

    # ball movement
    ball_x += ball_x_direction * ball_speed * dt
    ball_y += ball_y_direction * ball_speed * dt

    # ball collision

    # wall collision
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen.get_width():
        ball_x_direction *= -1
    if ball_y - ball_radius <= 0:
        ball_y_direction *= -1
    if ball_y + ball_radius >= screen.get_height():
        ball_x = screen.get_width() / 2
        ball_y = screen.get_height() / 2
        ball_x_direction = 1
        ball_y_direction = 1


    # paddle collision
    if ball_x + ball_radius >= paddle_left and ball_x - ball_radius <= paddle_left + paddle_width and ball_y + ball_radius >= paddle_top and ball_y - ball_radius <= paddle_top + paddle_height:
        ball_y_direction *= -1

    # resetting frame
    pygame.display.flip()


pygame.quit()