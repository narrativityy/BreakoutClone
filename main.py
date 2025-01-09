import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600), flags=pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill('black')

  pygame.display.flip()

  dt = clock.tick(60) / 1000

pygame.quit()