import pygame
class Scroll:
    def __init__(self, height, image):
        self.image = pygame.image.load(image).convert()
        self.coord = [0,0]
        self.coord2 = [0, -height]
        self.y_org = self.coord[1]
        self.y2_org = self.coord2[-1]

    def show(self, surface):
        surface.blit(self.image, self.coord)
        surface.blit(self.image, self.coord2)
    def update_coords(self, speed_y, time):
        distance_y = speed_y * time
        self.coord[1] += distance_y
        self.coord2[1] += distance_y
        if self.coord2[1] >= 0:
            self.coord[1] = self.y_org
            self.coord2[1] = self.y2_org