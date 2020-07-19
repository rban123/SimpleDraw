import pygame

class Circle():

    def __init__(self, surface, color, center, radius, width=0):
        self.surface = surface
        self.color = color
        self.center = center
        self.radius = radius
        self.width = width
        
    def update(self, surface, color, center, radius):
        self.surface = surface
        self.color = color
        self.radius = radius

    def update_center(self, center):
        self.center = center

    def update_radius(self, radius):
        self.radius = radius 

    def draw(self):
        try:
            pygame.draw.circle(self.surface, self.color, self.center, self.radius, self.width)    
        except:
            print("###########################\n####  Error: brush szie mustbe > 0 ####\n##########################")

