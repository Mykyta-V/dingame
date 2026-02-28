import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((900, 300))
pygame.display.set_caption("Dinosaur Game")
pygame.display.set_icon(pygame.image.load("images/bones.png"))
fonn = pygame.image.load("images/fonn.png")

bg_x = 0

Dino = pygame.image.load("images/dino.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(fonn, (bg_x, 0))
    screen.blit(fonn, (bg_x + 900, 0))
    screen.blit(Dino, (10, 195))
    pygame.display.update()

    bg_x -= 10
    if bg_x <= -900:
        bg_x = 0

    clock.tick(15)

pygame.quit()
sys.exit()
