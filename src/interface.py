import tkinter as tk
from tkinter import messagebox, Grid
from src.const import CONST

class Interface():
    def start_main_loop(self):
        self.root.mainloop()

    def setup(self, controller):
        self.controller = controller
        # Initialize Tkinter components
        self.main_window_init()
        self.on_resize_window()
        self.create_sudoku_boxes()
        self.create_solve_button()
        self.create_reset_button()
        self.grid_configurate()
        self.arrow_movement()
        
    def main_window_init(self):
        # Initialize Tkinter window
        self.root = tk.Tk()
        self.root.title('Sudoku solver')
        # Tkinter window properties (size, start position, background)
        self.window_width = 500
        self.window_height = 500
        self.root.update_idletasks()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.x_coord = self.screen_width//2 - self.window_width//2
        self.y_coord = self.screen_height//2 - self.window_height//2
        self.root.minsize(300, 300)
        self.root.geometry(f'{self.window_width}x{self.window_height}+{self.x_coord}+{self.y_coord}')
        self.root.configure(background='black')

    def create_sudoku_boxes(self):
        self.sudoku_entrytk = [[] for _ in range(CONST.SUDOKU_BOXES_NUM.value)]
        self.vcmd = (self.root.register(self.controller.box_entry_validate), '%S')
        for row in range(CONST.SUDOKU_BOXES_NUM.value):
            for col in range(CONST.SUDOKU_BOXES_NUM.value):
                self.box_entry = tk.Entry(self.root, validate='key', 
                                        vcmd=self.vcmd, justify='center', 
                                        borderwidth=1, relief='ridge',
                                        font=('Ubuntu', self.font_size*2)
                                      )
                self.box_entry.grid(row=row, column=col, 
                                padx=((col%3 == 0) * 2,  (col == 8) * 2), 
                                pady=((row%3 == 0) * 2,  (row == 8) * 2),
                                sticky='nsew')
                self.sudoku_entrytk[row].append(self.box_entry)

    def create_solve_button(self):
        self.solve_button = tk.Button(self.root, height=3, text='Solve!', 
                                    command=lambda: self.controller.solve_button_func(self.sudoku_entrytk),
                                    font=("Helvetica", self.font_size))
        self.solve_button.grid(row=CONST.SUDOKU_BOXES_NUM.value, 
                            columnspan=CONST.SUDOKU_BOXES_NUM.value//2+1,
                            sticky='nsew')

    def create_reset_button(self):
        self.reset_button = tk.Button(self.root, height=3, text='Reset!', 
                                command=self.clear_sudoku_boxes,
                                font=("Helvetica", self.font_size))
        self.reset_button.grid(row=CONST.SUDOKU_BOXES_NUM.value, 
                         column=CONST.SUDOKU_BOXES_NUM.value//2+1, 
                         columnspan=CONST.SUDOKU_BOXES_NUM.value//2, 
                         sticky='nsew')

    def show_sudoku_solution(self, sudoku_solution):
        for i, boxes_entry_row in enumerate(self.sudoku_entrytk):
            for j, box_entry in enumerate(boxes_entry_row):
                box_entry.delete(0, tk.END)
                box_entry.insert(0, sudoku_solution[i][j])

    def freeze_sudoku(self):
        self.solve_button.config(state=tk.DISABLED)
        for boxes_entry_row in self.sudoku_entrytk:
            for box_entry in boxes_entry_row:
                box_entry.config(state='disabled')

    def clear_sudoku_boxes(self):
        self.solve_button.config(state=tk.NORMAL)
        for boxes_entry_row in self.sudoku_entrytk:
            for box_entry in boxes_entry_row:
                box_entry.config(state='normal')
                box_entry.delete(0, tk.END)

    def grid_configurate(self):
        for x in range(CONST.SUDOKU_BOXES_NUM.value):
            Grid.columnconfigure(self.root, index=x, weight=1)
            Grid.rowconfigure(self.root, index=x, weight=1)        
            
    def arrow_movement(self):
        self.sudoku_entrytk[0][0].focus()
        for row in range(CONST.SUDOKU_BOXES_NUM.value):
            for col in range(CONST.SUDOKU_BOXES_NUM.value):
                # Add arrow movement properties on sudoku columns
                if col == 0:
                    self.sudoku_entrytk[row][col].bind('<Right>', lambda e, y=row, x=col: self.sudoku_entrytk[y][x+1].focus())
                    self.sudoku_entrytk[row][col].bind('<Left>', lambda e, y=row: self.sudoku_entrytk[y][-1].focus())
                if col == CONST.SUDOKU_BOXES_NUM.value-1:
                    self.sudoku_entrytk[row][col].bind('<Right>', lambda e, y=row: self.sudoku_entrytk[y][0].focus())
                    self.sudoku_entrytk[row][col].bind('<Left>', lambda e, y=row, x=col: self.sudoku_entrytk[y][x-1].focus())
                if 0 < col < CONST.SUDOKU_BOXES_NUM.value-1:
                    self.sudoku_entrytk[row][col].bind('<Right>', lambda e, y=row, x=col: self.sudoku_entrytk[y][x+1].focus())
                    self.sudoku_entrytk[row][col].bind('<Left>', lambda e, y=row, x=col: self.sudoku_entrytk[y][x-1].focus())
                # Add arrow movement properties on sudoku rows        
                if row == 0:
                    self.sudoku_entrytk[row][col].bind('<Up>', lambda e, x=col: self.sudoku_entrytk[-1][x].focus())
                    self.sudoku_entrytk[row][col].bind('<Down>', lambda e, y=row, x=col: self.sudoku_entrytk[y+1][x].focus())
                if row == CONST.SUDOKU_BOXES_NUM.value-1:
                    self.sudoku_entrytk[row][col].bind('<Up>', lambda e, y=row, x=col: self.sudoku_entrytk[y-1][x].focus())
                    self.sudoku_entrytk[row][col].bind('<Down>', lambda e, x=col: self.sudoku_entrytk[0][x].focus())
                if 0 < row < CONST.SUDOKU_BOXES_NUM.value-1:
                    self.sudoku_entrytk[row][col].bind('<Up>', lambda e, y=row, x=col: self.sudoku_entrytk[y-1][x].focus())
                    self.sudoku_entrytk[row][col].bind('<Down>', lambda e, y=row, x=col: self.sudoku_entrytk[y+1][x].focus())   

    def on_resize_window(self):
        # Tkinter window components resize properties
        self.resize_win_comp_step = 40
        self.font_size = self.window_height//self.resize_win_comp_step
        self.root.bind('<Configure>', lambda e: self.on_resize_window_func())

    def on_resize_window_func(self):
        if self.font_size == self.root.winfo_height()//self.resize_win_comp_step:
            return           
        self.font_size = self.root.winfo_height()//self.resize_win_comp_step
        self.resize_boxes_text()
        self.resize_solve_button_text()
        self.resize_reset_button_text()

    def resize_boxes_text(self):
        self.box_font_size = self.font_size*2
        for boxes_entry_row in self.sudoku_entrytk:
            for box_entry in boxes_entry_row:
                box_entry.config(font=('Ubuntu', self.box_font_size))

    def resize_solve_button_text(self):
        self.solve_button.config(font=("Helvetica", self.font_size))

    def resize_reset_button_text(self):
        self.reset_button.config(font=("Helvetica", self.font_size))

    def show_error(self, error):
        if error == 'wrong_number':
            messagebox.showerror('error', 'Enter numbers only from 1 to 9!')
        elif error == 'sudoku_issue':
            messagebox.showerror('error', 'The supplied sudoku has a issue!')
        elif error == 'no_solution':
            messagebox.showerror('error', 'There is no solution!')
        else:
            messagebox.showerror('error', 'This error is not implemented!')
            raise NotImplementedError('This error is not implemented!')








             


    

