import pygame
import sys
from cell import *
from sudoku_generator import *


class Board:
    def __init__(self, width, height, screen, initial_board):
        self.width = width
        self.height = height
        self.screen = screen
        self.initial_board = initial_board
        self.selected_cell = None
        self.cell_list = []

    def draw(self):
        num = 0
        for i in range(9):
            for j in range(9):
                self.cell_list[num].draw(self.width,self.height)
                while j <= 9:
                    # The x and  y coordinates increment by 1/9 of the width and height
                    x_coord = j * self.width/9
                    y_coord = j * self.height/9
                    # Every third line is bolded
                    if j % 3 == 0:
                        thickness = 4
                    else:
                        thickness = 2
                    pygame.draw.line(self.screen, (0, 0, 0), (x_coord, 0), (x_coord, self.height), thickness)
                    pygame.draw.line(self.screen, (0, 0, 0), (0, y_coord), (self.width, y_coord), thickness)
                    j += 1
                num+=1
        pygame.display.update()

    def select(self, row, col):
        for cell in self.cell_list:
            if ((cell.get_col() == col-1) and (cell.get_row()==row-1)):
                if(cell.get_type() == 0):
                    self.selected_cell = cell
                    x = (col - 1) * self.width/9
                    y = (row - 1) * self.height/9
                    pygame.draw.line(self.screen, (255, 0, 0), (x, y), (x + self.width/9, y), 2)
                    pygame.draw.line(self.screen, (255, 0, 0), (x, y), (x, y + self.height/9), 2)
                    pygame.draw.line(self.screen, (255, 0, 0), (x + self.width/9, y), (x + self.width/9, y + self.height/9), 2)
                    pygame.draw.line(self.screen, (255, 0, 0), (x, y + self.height/9), (x + self.width/9, y + self.height/9), 2)
                    pygame.display.update()
                    return 0
                elif(cell.get_type()==1):
                    x = (col - 1) * self.width/9
                    y = (row - 1) * self.height/9
                    pygame.draw.line(self.screen, (238, 210, 2), (x, y), (x + self.width/9, y), 2)
                    pygame.draw.line(self.screen, (238, 210, 2), (x, y), (x, y + self.height/9), 2)
                    pygame.draw.line(self.screen, (238, 210, 2), (x + self.width/9, y), (x + self.width/9, y + self.height/9), 2)
                    pygame.draw.line(self.screen, (238, 210, 2), (x, y + self.height/9), (x + self.width/9, y + self.height/9), 2)
                    pygame.display.update()
                    return 1

    def click(self, x, y):
        range_of_coordx = self.width/9
        range_of_coordy = self.height/9
        i = 1
        if x > self. width or y > self.height:
            return None
        else:
            while i <= 9:
                if (i-1) * range_of_coordy < y < (i * range_of_coordy):
                    row = i
                    break
                i += 1
            i = 1
            while i <= 9:
                if (i-1) * range_of_coordx < x < (i * range_of_coordx):
                    col = i
                    break
                i += 1
        return row, col

    def clear(self):
        self.selected_cell.set_sketched_value(0)
        self.selected_cell.set_cell_value(0)
    def sketch(self, value):
        self.selected_cell.set_sketched_value(value)
        self.selected_cell.draw(self.width,self.height)

    def place_number(self, value):
        self.selected_cell.set_cell_value(value)

    def reset_to_original(self):
        for cell in self.cell_list:
            if cell.get_type() == 0:
                cell.set_cell_value(0)
                cell.set_sketched_value(0)

    def is_full(self):
        for cell in self.cell_list:
            if cell.get_value() == 0:
                return False
        return True

    def check_board(self,solution_board):
        num = 0
        for i in solution_board:
            if i != self.cell_list[num].get_value():
                return False
            num += 1
        return True

    def set_initial_board(self):
        for i in range(9):
            for j in range(9):
                value = self.initial_board[i][j]
                if value == 0:
                    individual_cell = Cell(value, i, j, self.screen,0)
                elif value > 0:
                    individual_cell = Cell(value,i,j,self.screen,1)
                self.cell_list.append(individual_cell)
