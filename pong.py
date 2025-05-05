import pygame
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()

# Rectangles
rect_1 = pygame.Rect(100, 300, 10, 100)
rect_2 = pygame.Rect(1160, 300, 10, 100)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)

# Ball
ball = pygame.Rect(640, 360, 20, 20)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1) clear screen
    screen.fill(BLACK)

    # 2) draw paddles
    pygame.draw.rect(screen, WHITE, rect_1)
    pygame.draw.rect(screen, WHITE, rect_2)

    # 3) draw ball
    pygame.draw.rect(screen, BLUE, ball)

    # 4) Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rect_1.y -= 5
    if keys[pygame.K_s]:
        rect_1.y += 5
    if keys[pygame.K_UP]:
        rect_2.y -= 5
    if keys[pygame.K_DOWN]:
        rect_2.y += 5

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

