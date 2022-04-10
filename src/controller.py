from src.const import CONST

class Controller():
    def __init__(self, model, interface): 
        self.model = model
        self.interface = interface

    @staticmethod
    def box_entry_validate(box_entry):
        if box_entry not in ('', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            return False
        return True

    def boxes_entry_validate(self, sudoku_entrytk):
        for boxes_entry_row in sudoku_entrytk:
            for box_entry in boxes_entry_row:
                if not self.box_entry_validate(box_entry.get()):
                    return False
        return True

    def pull_sudoku(self, sudoku_entrytk):
        self.input_sudoku = [[] for _ in range(CONST.SUDOKU_BOXES_NUM.value)]
        for i, boxes_entry_row in enumerate(sudoku_entrytk):
            for box_entry in boxes_entry_row:
                entry = 0 if box_entry.get() == '' else int(box_entry.get())
                self.input_sudoku[i].append(entry)

    def solve_button_func(self, sudoku_entrytk):
        # Check if provided numbers are correct
        if not self.boxes_entry_validate(sudoku_entrytk):
            self.interface.show_error('wrong_number')
            return

        # Save provided sudoku input in a list
        self.pull_sudoku(sudoku_entrytk)

        # Check if provided sudoku is correct
        if not self.model.sudoku_first_check(self.input_sudoku):
            self.interface.show_error('sudoku_issue')
            return

        # Solve sudoku and check if there is a solution
        if not self.model.sudoku_solver(self.input_sudoku):
            self.interface.show_error('no_solution')
            return

        # Show sudoku solution
        self.interface.show_sudoku_solution(self.input_sudoku)
        self.interface.freeze_sudoku()

    def start_app(self):
        self.interface.setup(self)
        self.interface.start_main_loop()