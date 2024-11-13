import pygame
import time
from random import shuffle

pygame.init()

game_window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Click")
background = pygame.transform.scale(pygame.image.load("background.jpg"), (500, 500))

fps = pygame.time.Clock()

class Card:
    def __init__(self, filename1, filename2, x, y, width=70, height=70):
        self.index = filename1[0]
        self.area = pygame.Rect(x, y, width, height)
        self.picture1 = pygame.image.load(filename1)
        self.picture2 = pygame.image.load(filename2)
        self.click = False

    def drawing(self):
        if self.click:
            game_window.blit(self.picture1, (self.area.x, self.area.y))
        else:
            game_window.blit(self.picture2, (self.area.x, self.area.y))

    def collide(self, x, y):
        return self.area.collidepoint(x, y)

cards_image = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png"]
cards_image = cards_image * 2
shuffle(cards_image)

cards = []

x_start = 65
y_start = 115

for j in range(3):
    y = y_start + (100 * j)
    x = x_start
    for i in range(4):
        card = Card(cards_image[len(cards_image) - 1], "back.png", x, y)
        cards.append(card)
        cards_image.pop(len(cards_image) - 1)
        x += 100

start_game_time = time.time()
can_click = False
is_start_game = True

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and can_click:
            x, y = event.pos
            for card in cards:
                if card.collide(x, y):
                    card.click = True
                card.drawing()

    if time.time() - start_game_time > 3 and is_start_game:
        for card in cards:
            card.click = True
    if time.time() - start_game_time > 7 and is_start_game:
        for card in cards:
            card.click = False
        can_click = True
        is_start_game = False

    game_window.blit(background, (0, 0))
    for card in cards:
        card.drawing()
    pygame.display.flip()
    fps.tick(40)
