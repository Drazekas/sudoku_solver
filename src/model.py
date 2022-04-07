board = [
    [2,8,0,7,0,0,5,0,0],
    [4,0,0,0,0,0,3,0,0],
    [3,0,7,0,0,5,0,1,0],
    [0,0,8,0,9,0,6,0,3],
    [1,3,0,0,5,0,9,2,0],
    [7,0,0,0,0,2,0,0,0],
    [0,0,5,8,2,1,0,0,6],
    [6,7,0,0,4,3,1,8,5],
    [0,0,3,0,0,0,0,0,0]
]



def sudoku_solver(board):
    empty_field = find_empty(board)
    if not empty_field:
        return True
    row, col = empty_field
    for number in range(1,10):
        if valid_number(board, number, (row, col)):
            board[row][col] = number
            if sudoku_solver(board):
                return True
            board[row][col] = 0
    return False

def find_empty(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)
    return None

def valid_number(board, num, pos):
    # Check row
    for col in range(len(board)):
        if board[pos[0]][col] == num and pos[1] != col:
            return False

    # Check column    
    for row in range(len(board)):
        if board[row][pos[1]] == num and pos[0] != row:
            return False  

    # Check 3x3 cube
    box_row, box_col = pos[0]//3*3, pos[1]//3*3
    for row in range(box_row, box_row+3):
        for col in range(box_col, box_col+3):
            if board[row][col] == num and pos != (row,col):
                return False
    
    # return True if every condition is true
    return True

def print_board(board):
    for row in range(len(board)):
        if row % 3 == 0 and row != 0:
            print("- - - - - - - - - - - - - ")

        for col in range(len(board[0])):
            if col % 3 == 0 and col != 0:
                print(" | ", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col]) + " ", end="")


def run():
    print_board(board)
    print()
    sudoku_solver(board)
    print_board(board)
