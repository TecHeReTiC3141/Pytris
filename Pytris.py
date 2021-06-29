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
            pygame.draw.rect(display, self.color, (seg[0][0], seg[1][0], 50, 50))
        if self.chosen:
            pygame.draw.rect(display, (200, 200, 200), (self.segments[:, 0].min() - 5, self.segments[:, 1].min() - 5,
                                                        self.segments[:, 0].max() - self.segments[:, 0].min() + 10,
                                                        self.segments[:, 1].max() - self.segments[:, 1].min() + 10), 2)


def generate():
    y = 0
    x = random.randrange(50, 700, 50)
    generator_key = random.randint(1, 4)
    if generator_key == 1:
        '''
        # #
        # #
        '''
        seg = np.array([[list(range(x, x + 50)), list(range(y, y + 50))], [list(range(x + 50, x + 100)), list(range(y, y + 50))],
                        [list(range(x + 50, x + 100)), list(range(y + 50, y + 100))], [list(range(x, x + 50)), list(range(y + 50, y + 100))]])
    elif generator_key == 2:
        '''
          #
        # #
        #'''
        seg = np.array([[list(range(x, x + 50)), list(range(y, y + 50))], [list(range(x + 50, x + 100)), list(range(y, y + 50))],
                        [list(range(x + 50, x + 100)), list(range(y - 50, y))], [list(range(x, x + 50)), list(range(y + 50, y + 100))]])
    elif generator_key == 3:
        '''
        #
        #
        #
        #'''
        seg = np.array([[list(range(x, x + 50)), list(range(y, y + 50))], [list(range(x, x + 50)), list(range(y + 50, y + 100))],
                        [list(range(x, x + 50)), list(range(y + 100, y + 150))], [list(range(x, x + 50)), list(range(y + 150, y + 200))]])
    else:
        '''# # # #'''
        seg = np.array([[list(range(x, x + 50)), list(range(y, y + 50))], [list(range(x + 50, x + 100)), list(range(y, y + 50))],
                        [list(range(x + 100, x + 150)), list(range(y, y + 50))], [list(range(x + 150, x + 200)), list(range(y, y + 50))]])
    pytris_list.append(Pytris(seg, (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for pytr in pytris_list:
                for i in pytr.segments:
                    if event.pos[0] in i[0] and event.pos[1] in i[1]:
                        for p in pytris_list:
                            p.chosen = False
                        pytr.chosen = True
                        break

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
