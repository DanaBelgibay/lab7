import os
import pygame


pygame.mixer.init()
sound = pygame.mixer.music


WORKING = os.getcwd()
WORKING = os.path.join(WORKING, 'music')
q = []
for i in os.listdir(WORKING):
    q.append('music' + '/' + i)


#check
sound.load(q[0])
sound.play(0)
sound.pause()

class Button(pygame.sprite.Sprite):
    def __init__(self, image, coords):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = coords


class Pause(Button):
    def __init__(self, image, coords):
        super().__init__(image, coords)
        self.status = False
        self.coords = coords
        self.last_click = pygame.time.get_ticks()
        self.last_upd = self.last_click

    def update(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            now = pygame.time.get_ticks()
            if now - self.last_click >= 120:
                if self.status == True:
                    self.status = False
                    sound.unpause()
                else:
                    self.status = True
                    sound.pause()
                self.last_click = now
        if self.status:
            self.image = play_img
            self.rect = self.image.get_rect()
            self.rect.center = self.coords
        else:
            self.image = pause_img
            self.rect = self.image.get_rect()
            self.rect.center = self.coords
    
    def change_status(self):
        pass


class ForwardButton(Button):
    def __init__(self, image, coords):
        super().__init__(image, coords)
        self.last_click = pygame.time.get_ticks()

    def update(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            now = pygame.time.get_ticks()
            if now - self.last_click >= 120:
                global q
                q = q[1:] + [q[0]]
                sound.load(q[0])
                sound.play(0)
                if pause.status:
                    sound.pause()
                self.last_click = now


class PrevButton(Button):
    def __init__(self, image, coords):
        super().__init__(image, coords)
        self.last_click = pygame.time.get_ticks()

    def update(self):
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            now = pygame.time.get_ticks()
            if now - self.last_click >= 120:
                global q
                q = [q[-1]] + q[:len(q) - 1]
                sound.load(q[0])
                sound.play(0)
                if pause.status:
                    sound.pause()
                self.last_click = now


pause_img = pygame.image.load('music_player/pause.png')
play_img = pygame.image.load('music_player/play-button.png')
forward_img = pygame.image.load('music_player/forwards.png')
prev_img = pygame.transform.rotate(forward_img, 180)


WIDTH, HEIGHT = 640, 150
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()


pause = Pause(play_img, (315, 75))
all_sprites.add(ForwardButton(forward_img, (390, 75)))
all_sprites.add(pause)
all_sprites.add(PrevButton(prev_img, (240, 75)))
app = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((250, 250, 250))
    clock.tick(30)

    
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.display.update()


