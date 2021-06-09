# B.Woodfield / RaserSharp
# Verses from the Dhammapada
# A book written from a collection of wise sayings in Buddhism
# The sayings were from Siddartha Gautama - or as we know him - Buddha
#
# The book is freely available for non-profit copying and sharing
# I have included Every verse from all of the chapters.
#
# This GUI version allows the user to click a button to see a random verse
# and displays the text in the Shell window.
#
# Written in Python 3
# Uses Tkinter - needs no additional modules installed

import random
import tkinter as tk
from tkinter import *

class MainApplication(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)  
        self.parent = parent
            
        def random_line():
            line_num = 0
            selected_line = ''
            with open('dhammapada.txt') as f:
                while 1:
                    line = f.readline()
                    if not line: break
                    line_num += 1 
                    if random.uniform(0, line_num) < 1:
                        selected_line = line
            return(selected_line.strip())         


        def print_a_verse():
            print('\n',random_line())

        btn_result = Button(self, fg='Gold', text='New Verse', bg='Black', font='freesansbold, 16', command=print_a_verse) #textvariable=cvt_to, font='freesansbold, 16', fg='Blue')
        btn_result.pack(fill=X,side=BOTTOM)#fill=BOTH, expand=1)

        lbl_one = Label(self, bg='DarkGrey', fg='White',  text='Dhammapada', font='freesansbold, 22')
        lbl_one.pack(fill=BOTH, expand=1)

        lbl_thr = Label(self, bg='DarkGrey', fg='White', text='The Dhammapada \nSiddartha Gautama - Buddha', font='freesansbold, 18')
        lbl_thr.pack(fill=BOTH, expand=1)

        lbl_two = Label(self, bg='DarkGrey', fg='Grey')
        lbl_two.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(400,400)
    #root.configure(bg='Black')
    root.title('Python - Dhammapada Verses')
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
