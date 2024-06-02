import pygame
class Group(pygame.sprite.Group):
    def update(self):
        for Object in self.sprites():
            Object.update()