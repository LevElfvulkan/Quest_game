import pygame


class BackGr(pygame.sprite.Sprite):
    def __init__(self, image_path , position):
        super().__init__()
        self.image = pygame.image.load(image_path )
        self.position = position
    def draw(self  , screen):
        screen.blit(self.image , self.position)