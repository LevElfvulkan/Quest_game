import pygame
from classes.player import Player
from classes.bg import BackGr
from classes.enemy import Enemy

pygame.init()
screen = pygame.display.set_mode((800, 800) )
pygame.display.set_caption("Квест-игра")


bg = BackGr('Image/craiyon_223618_2d_rocky_mountain_background_for_2d_game.png' , (0 , 0))
player = Player('Image/2D Game Character Sprites  (2).jpg' , (300,300) )

def main():
    running = False
    while not running:
        bg.draw(screen)
        player.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
                pygame.quit()
main()













