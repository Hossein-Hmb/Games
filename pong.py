import pygame


# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1280, 720))
running = True
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)

# Game variables
PADDLE_SPEED = 10
BALL_SPEED = 2
SPEED_BOOST = 1.1

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.rect.clamp_ip(screen.get_rect())

    def move(self, up, down):
        if up:
            self.rect.y -= 5
        if down:
            self.rect.y += 5

class Ball:
    def __init__(self, x, y, radius):
        self.rect = pygame.Rect(x, y, radius, radius)
        self.x = BALL_SPEED
        self.y = BALL_SPEED

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def move(self):
        self.rect.x += self.x
        self.rect.y += self.y

# Rectangles
rect_1 = Paddle(100, 300, 10, 100, WHITE)
rect_2 = Paddle(1160, 300, 10, 100, WHITE)

# Ball
ball = Ball(640, 360, 20)

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
    pygame.draw.rect(screen, BLUE, ball.rect)

    # 4) Move paddles
    keys = pygame.key.get_pressed()
    rect_1.move(keys[pygame.K_w], keys[pygame.K_s])
    rect_2.move(keys[pygame.K_UP], keys[pygame.K_DOWN])

    # 5) Move ball
    ball.move()

    # 6) Check for collisions
    if ball.rect.colliderect(rect_1) or ball.rect.colliderect(rect_2):
        ball.x *= -SPEED_BOOST
        ball.y *= SPEED_BOOST

    # 7) Check for out of bounds
    if ball.rect.y < 0 or ball.rect.y > 720:
        ball.y *= -1

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

