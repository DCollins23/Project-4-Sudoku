# Program imports the math and random modules.
import math
import random


class SudokuGenerator:
    def __init__(self, row_length, removed_cells):
        # Program initializes SudokuGenerator object with a specified row length and number of cells to be removed.
        self.row_length = row_length
        self.removed_cells = removed_cells
        # Program initializes the Sodoku board as a 2D list with all elements set to zero.
        self.board = [[0 for _ in range(row_length)] for _ in range(row_length)]
        # Program calculates the length of the board within the Sodoku grid.
        self.box_length = int(math.sqrt(row_length))
        '''
        Notes:
        - The row length will always be 9 for this project.
        - removed_cells should equal 30 for easy, 40 for medium, and 50 for hard
        '''

    def get_board(self):
        # Program returns a 2D list of numbers representing the current state of the board.
        return self.board

    def print_board(self):
        # Program prints the current state of the board to the console.
        for row in self.board:
            print(" ".join(map(str, row)))

        '''
        Notes:
        - Not strictly required. Can be used for debugging.
        '''

    def valid_in_row(self, row, num):
        # Program determines if the given number is in the specified row of the board and returns True or False.
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        # Program determines if the given number is in the specified column of the board and returns True or False.
        return num not in [self.board[row][col] for row in range(self.row_length)]

    def valid_in_box(self, row_start, col_start, num):
        # Program determines if the given number is in the specified 3x3 box.
        for i in range(self.box_length):
            for j in range(self.box_length):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        # Program determines if it is even valid to enter a number at the specified (row, col) of the board.
        # Notes: A user cannot enter a number in a place that was randomly filled by the program.
        return (
            self.valid_in_row(row, num) and
            self.valid_in_col(col, num) and
            self.valid_in_box(row - row % self.box_length, col - col % self.box_length, num)
        )

    def fill_box(self, row_start, col_start):
        # Program fills the specified box with random values.
        # Note to self: Figure out if unused_in_box needs to be used.
        box_values = [i for i in range(1, self.row_length + 1)]
        for i in range(self.box_length):
            for j in range(self.box_length):
                while True:
                    # Program generates a random digit for the current position in the box.
                    num = random.choice(box_values)
                    if self.valid_in_box(row_start, col_start, num):
                        # Program places a valid number in the box and removes it from the available values.
                        self.board[row_start + i][col_start + j] = num
                        box_values.remove(num)
                        break

    def fill_diagonal(self):
        # Program fills the 3 boxes along the main diagonal of the board.
        for i in range(0, self.row_length, self.box_length):
            self.fill_box(i, i)

    def fill_remaining(self, row, col):
        # Program returns a completely filled board via backtracking.
        # This code was provided and unchanged.
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):
        # Program fills the entire board (solution) by calling the fill_diagonal and fill_remaining methods.
        # This code was provided and unchanged.
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)
        final_solution = []
        for i in self.board:
            for j in i:
                final_solution.append(j)
        return final_solution


    def remove_cells(self):
        # Program removes the appropriate number of cells from the board by setting random cells to 0.
        # Program also ensures that a cell cannot be removed more than once.
        cells_to_remove = self.removed_cells
        while cells_to_remove > 0:
            row = random.randint(0, self.row_length - 1)
            col = random.randint(0, self.row_length - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                cells_to_remove -= 1


# Program generates and returns a Sudoku board with specified size and number of cells removed.
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    board_two = sudoku.fill_values()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board,board_two
