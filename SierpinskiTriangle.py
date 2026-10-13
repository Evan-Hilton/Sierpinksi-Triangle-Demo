import pygame
import sys
import random as rng

# Basic config
WIDTH = 720 * 2
HEIGHT = 450 * 2
FRAME_RATE = 60

# Initialize Variables Here
x = []
y = []
ballRadius = 1
xstart = WIDTH / 2
ystart = HEIGHT / 2
x_ = [WIDTH / 2, 200, WIDTH - 200]
y_ = [100, HEIGHT - 100, HEIGHT - 100]

# make sure to initialize all used variables in this method as global
def initialize():
    global x
    global y
    x.append(xstart)
    y.append(ystart)

# make sure to initialize all used variables in this method as global
def main_loop():
    global x
    global y
    global x_
    global y_
    choice = rng.randint(0, 2)

    x.append(abs((x[-1] - x_[choice])/2) + min(x[-1], x_[choice]))
    y.append(abs((y[-1] - y_[choice])/2) + min(y[-1], y_[choice]))

# make sure to initialize all used variables in this method as global
def paint_loop(screen):
    global x_
    global y_
    global x
    global y
    screen.fill((0, 0, 0))  # background

    triangle = [(x_[0], y_[0]), (x_[1], y_[1]), (x_[2], y_[2])]
    for i in range(len(x)):
        pygame.draw.circle(screen, (255, 255, 255), (x[i], y[i]), ballRadius)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Python Graphics Template")
    clock = pygame.time.Clock()

    initialize()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        main_loop()
        paint_loop(screen)

        pygame.display.flip()
        clock.tick(FRAME_RATE)

if __name__ == "__main__":
    main()