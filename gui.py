from tkinter import *


class GUI:
    def __init__(self, window):
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text="Pick a shape to find it's area!")
        self.label_name.pack()
        self.frame_name.pack()

        self.frame_middle = Frame(self.window)
        self.label_name2 = Label(self.frame_middle, text='Shape:')
        self.radio_1 = IntVar()
        self.radio_1.set(-1)
        self.radio_circle = Radiobutton(self.frame_middle, text='Circle', variable=self.radio_1, value=0)
        self.radio_rectangle = Radiobutton(self.frame_middle, text='Rectangle', variable=self.radio_1, value=1)
        self.radio_square = Radiobutton(self.frame_middle, text='Square', variable=self.radio_1, value=2)
        self.radio_triangle = Radiobutton(self.frame_middle, text='Triangle', variable=self.radio_1, value=3)
        self.label_name2.pack(padx=5, side='left')
        self.radio_circle.pack(side='left')
        self.radio_rectangle.pack(side='left')
        self.radio_square.pack(side='left')
        self.radio_triangle.pack(side='left')
        self.frame_middle.pack()

        self.frame_bottom = Frame(self.window)
        self.button_enter = Button(self.frame_bottom, text='Enter', command=self.clicked)
        self.button_enter.pack()
        self.frame_bottom.pack()

    def clicked(self):
        shape = self.radio_1.get()


