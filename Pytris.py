import pygame, random, numpy as np

pygame.init()

display = pygame.display.set_mode((1000, 750))
pygame.display.set_caption('Pytris')
title_font = pygame.font.Font(None, 86)
clock = pygame.time.Clock()
pytris_list = []
tick = 0


class Pytris:

    def __init__(self, segments, color, chosen=False):
        self.segments = segments
        self.color = color
        self.chosen = chosen

    def fly(self):
        for i in self.segments:
            i[1] += 50

    def draw_object(self):
        for seg in self.segments:
            pygame.draw.rect(display, self.color, (seg[0], seg[1], 50, 50))


def generate():
    y = 0
    x = random.randrange(50, 700, 50)
    generator_key = random.randint(1, 4)
    if generator_key == 1:
        seg = np.array([[x, y], [x + 50, y], [x + 50, y + 50], [x, y + 50]])
    elif generator_key == 2:
        seg = np.array([[x, y], [x + 50, y], [x + 50, y - 50], [x, y + 50]])
    elif generator_key == 3:
        seg = np.array([[x, y], [x, y + 50], [x, y + 100], [x, y + 150]])
    else:
        seg = np.array([[x, y], [x + 50, y], [x + 100, y], [x + 150, y]])
    pytris_list.append(Pytris(seg, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    display.fill((10, 10, 10))
    pygame.draw.rect(display, (200, 200, 200), (50, 100, 700, 600), 5)

    for pyt in pytris_list:
        pyt.draw_object()
        if not tick % 60:
            pyt.fly()
    pygame.draw.rect(display, (10, 10, 10), (50, 0, 700, 100))
    pygame.draw.rect(display, (10, 10, 10), (50, 700, 700, 100))
    display.blit(title_font.render('Pytris', True, (200, 200, 200)), (50, 25))
    pygame.display.update()
    clock.tick(60)

    if not random.randint(0, 300):
        generate()
    tick += 1
