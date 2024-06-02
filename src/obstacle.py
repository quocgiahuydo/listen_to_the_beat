import pygame
class Obstacle(pygame.sprite.Sprite):
    def __init__(self,image,pos_x,pos_y ):
        super().__init__()
        self.image=pygame.Surface([700,50])
        self.image=pygame.image.load(image)
        self.rect=self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y
    def update(self,img,new_x_pos,new_y_pos) :
        self.image=pygame.image.load(img)
        self.rect.x=new_x_pos
        self.rect.y=new_y_pos