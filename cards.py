import pygame
from random import shuffle


pygame.init()

game_window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Cards")
background = pygame.image.load("background.jpg")
game_window.blit(background, (0, 0))

fps = pygame.time.Clock()


class Card:
    def __init__(self, filename1, filename2, x, y, width=70, height=70):
        self.index = filename1[0]
        self.area = pygame.Rect(x, y, width, height)
        self.picture1 = pygame.image.load(filename1)
        self.picture2 = pygame.image.load(filename2)
        self.click = True

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
        card = Card(cards_image[j * 4 + i], 'back.png', x, y)
        cards.append(card)
        x += 100

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    game_window.blit(background, (0, 0))
    for card in cards:
        card.drawing()
    pygame.display.update()
    fps.tick(40)
