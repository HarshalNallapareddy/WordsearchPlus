from re import sub
from tkinter import CENTER, Tk, Frame, Label, Button, Entry

from sqlalchemy import column

word_board = []
words = []

def input_edit(text, word_list):
    
    word_board = []
    def start(text, word_list):

        root = Tk()

        frame1 = Frame(root, padx=5, pady=5)
        frame1.grid(row=0, column=0)

        rows = len(text)
        cols = len(text[0])

        word_board_entries = []
        word_list_entries = []

        #letter grid 
        for i in range(rows):
            entry_row = []
            for j in range(cols):
                entry = Entry(frame1, width=3)
                entry.insert(0, text[i][j])
                entry.grid(row=i, column=j, padx=3, pady=3)
                entry_row.append(entry)
            word_board_entries.append(entry_row)

        #add/del row/col/word methods
        def add_row():
            entry_row = []
            nonlocal rows
            for n in range(cols):
                entry = Entry(frame1, width=3)
                entry.grid(row=rows, column=n, padx=3, pady=3)
                entry_row.append(entry)
            word_board_entries.append(entry_row)
            rows += 1
        
        def add_col():
            nonlocal cols
            for n in range(rows):
                entry = Entry(frame1, width=3)
                entry.grid(row=n, column=cols, padx=3, pady=3)
                word_board_entries[n].append(entry)
            cols += 1

        def del_row():
            nonlocal rows
            for w in frame1.grid_slaves(rows - 1):
                w.grid_forget()
            rows -= 1
            del word_board_entries[-1]

        def del_col():
            nonlocal cols
            i = 0
            for w in frame1.grid_slaves(None, cols - 1):
                w.grid_forget()
                del word_board_entries[i][-1]
                i += 1
            cols -= 1

        def add_word():
            entry = Entry(frame3, width=15)
            entry.grid(row=(len(word_list_entries) % len(text)), column=(len(word_list_entries) // len(text)), padx=3, pady=3)
            word_list_entries.append(entry)

        def del_word():
            frame3.grid_slaves(row=None, column=((len(word_list_entries) - 1) // len(text)))[0].grid_forget()
            del word_list_entries[-1]

        #submit grid into 2-d array method
        def submit_grid():
            for i in range(rows):
                None_row = [None] * (cols)
                word_board.append(None_row)
            
            for x in range(rows):
                for y in range(cols):
                    word_board[x][y] = str(word_board_entries[x][y].get()).upper()

            for entry in word_list_entries:
                words.append(str(entry.get()).upper())

            root.destroy()

        #add/del row/col buttons
        frame2 = Frame(root, padx=5, pady=5)
        frame2.grid(row=1, column=0)
        button1 = Button(frame2, text='Add Row', command=add_row)
        button2 = Button(frame2, text='Add Column', command=add_col)
        button3 = Button(frame2, text='Delete Row', command=del_row)
        button4 = Button(frame2, text='Delete Column', command=del_col)
        button1.pack(padx=5, side='left')
        button2.pack(padx=5, side='left')
        button3.pack(padx=5, side='left')
        button4.pack(padx=5, side='left')

        #submit button
        submit = Button(frame2, text='Submit', bg='green', command=submit_grid)
        submit.pack(padx=5, side='right')

        #word_list input/edit frame
        frame3 = Frame(root, padx=5, pady=5)
        frame3.grid(row=0, column=1)

        for n in range(len(word_list)):
            entry = Entry(frame3, width=15, justify=CENTER)
            entry.insert(0, word_list[n])
            entry.grid(row= (n % len(text)), column= (n // len(text)), padx=3, pady=3)
            word_list_entries.append(entry)

        #add/del word buttons
        frame4 = Frame(root, padx=5, pady=5)
        frame4.grid(row=1, column=1)
        button5 = Button(frame4, text='Add Word', command=add_word)
        button5.pack(padx=5)
        button6 = Button(frame4, text='Delete Word', command=del_word)
        button6.pack(padx=5)

        root.mainloop()

    start(text, word_list)
    return (word_board, words)

def output(word_board, word_coords):
    root = Tk()

    frame5 = Frame(root, padx=5, pady=5)
    frame5.pack()

    for x in range(len(word_board)):
        for y in range(len(word_board[0])):
            label = Label(frame5, text=word_board[x][y], width=3)
            label.grid(row=x, column=y, padx=3, pady=3)
            if (x, y) in word_coords:
                label.config(bg='yellow')

    root.mainloop()
    