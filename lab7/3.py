import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        pygame.draw.circle(self.image, color='BLUE', center=self.rect.center, radius=25)
    
    def update(self):
        temp = pygame.key.get_pressed()
        if temp[pygame.K_UP]:
            x, y = self.rect.center[0], max(25, self.rect.center[1] - 20)
            self.rect.center = (x, y)
        if temp[pygame.K_DOWN]:
            x, y = self.rect.center[0], min(615, self.rect.center[1] + 20)
            self.rect.center = (x, y)
        if temp[pygame.K_LEFT]:
            x, y = max(25, self.rect.center[0] - 20), self.rect.center[1]
            self.rect.center = (x, y)
        if temp[pygame.K_RIGHT]:
            x, y = min(615, self.rect.center[0] + 20), self.rect.center[1]
            self.rect.center = (x, y)


WIDTH, HEIGHT = 640, 640
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game = True
all_sprites = pygame.sprite.Group()
pl = Player()
all_sprites.add(pl)


while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    screen.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    

    clock.tick(30)
    pygame.display.flip()
    pygame.display.update()


pygame.quit()