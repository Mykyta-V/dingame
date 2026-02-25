import pygame

clock = pygame.time.Clock()

pygame.init()
screen = pygame.display.set_mode((900, 300))
pygame.display.set_caption("Dinosaur Game")
pygame.display.set_icon(pygame.image.load("images/bones.png"))
fon = pygame.image.load("images/fon.png")

bg_x = 0

Dino = pygame.image.load("images/dinosaur.png")

running = True
while running:
    screen.blit(fon, (bg_x, 0))
    screen.blit(fon, (bg_x + 900, 4))
    screen.blit(Dino, (10, 230))
    pygame.display.update()


    bg_x -= 10
    if bg_x <= -900:
        bg_x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    clock.tick(15)
