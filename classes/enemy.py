import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self , image_path , position):
        self.image = pygame.image.load(image_path)
        self.position = position

    def draw(self , screeen):
        screeen.blit(self.image , self.position)