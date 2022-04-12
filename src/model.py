from xmlrpc.client import Boolean
from src.const import CONST

class Model():
    def find_empty_box(self, 
                    input_sudoku: list[list[int]]) -> tuple[int, int] | None:
        for row in range(CONST.SUDOKU_BOXES_NUM.value):
            for col in range(CONST.SUDOKU_BOXES_NUM.value):
                if input_sudoku[row][col] == 0:
                    return (row, col)
        return None

    def valid_number(self, input_sudoku: list[list[int]], 
                     num: int, pos: int) -> bool:
        # Check if the number is correct within the position.
        # Check row
        for col in range(CONST.SUDOKU_BOXES_NUM.value):
            if input_sudoku[pos[0]][col] == num and pos[1] != col:
                return False
        # Check column    
        for row in range(CONST.SUDOKU_BOXES_NUM.value):
            if input_sudoku[row][pos[1]] == num and pos[0] != row:
                return False  
        # Check 3x3 square
        square_first_row, square_first_col = pos[0]//3*3, pos[1]//3*3
        for row in range(square_first_row, square_first_row+3):
            for col in range(square_first_col, square_first_col+3):
                if input_sudoku[row][col] == num and pos != (row,col):
                    return False
        # return True if every condition is true
        return True

    def sudoku_first_check(self, input_sudoku: list[list[int]]) -> bool:
        # Check if provided sudoku is correct
        for row in range(CONST.SUDOKU_BOXES_NUM.value):
            for col in range(CONST.SUDOKU_BOXES_NUM.value):
                if input_sudoku[row][col] != 0:
                    if not self.valid_number(input_sudoku, 
                                             input_sudoku[row][col], 
                                             (row,col)):
                        return False
        return True

    def sudoku_solver(self, input_sudoku: list[list[int]]) -> bool:
        # Solve sudoku with a recursion backtracking algorithm
        empty_box: tuple[int, int] | None = self.find_empty_box(input_sudoku)
        if not empty_box:
            return True
        row, col = empty_box
        for number in range(1,10):
            if self.valid_number(input_sudoku, number, (row, col)):
                input_sudoku[row][col] = number
                if self.sudoku_solver(input_sudoku):
                    return True
                input_sudoku[row][col] = 0
        return False        