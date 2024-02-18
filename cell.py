import pygame
import sys
class Cell():
    def __init__(self, value, row, col, screen,type):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.type = type
        self.sketched_value = None
    def get_value(self):
        return self.value
    def get_sketched_value(self):
        return self.sketched_value
    def get_row(self):
        return self.row
    def get_col(self):
        return self.col
    def get_type(self):
        return self.type
    def set_cell_value(self,value):
        self.value = value
        self.sketched_value = 0
    def set_sketched_value(self,value):
        self.sketched_value = value
        self.value = 0
    def draw(self,width,height):
        if (self.sketched_value != None and self.sketched_value > 0):
            num_font = pygame.font.Font(None, 40)
            num_surf = num_font.render(str(self.sketched_value), 0, (147, 151, 153))
            num_rect = num_surf.get_rect(center=(((self.col) * width/9) + width / 36,((self.row) * height/9) + height / 36))
            self.screen.blit(num_surf, num_rect)
        if (self.value!= None and self.value > 0):
            if(self.type == 0):
                x = (self.col * width / 9) + width / 18
                y = (self.row * height / 9) + height / 18
                num_font = pygame.font.Font(None, 50)
                num_surf = num_font.render(str(self.value), 0, (127, 0, 255))
                num_rect = num_surf.get_rect(center=(x, y))
                self.screen.blit(num_surf, num_rect)
            if(self.type ==1):
                x = (self.col * width / 9) + width / 18
                y = (self.row * height / 9) + height / 18
                num_font = pygame.font.Font(None, 50)
                num_surf = num_font.render(str(self.value), 0, (0, 0, 0))
                num_rect = num_surf.get_rect(center=(x, y))
                self.screen.blit(num_surf, num_rect)
        pygame.display.update()
