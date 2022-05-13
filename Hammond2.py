from gui import *


def main():
    window = Tk()
    window.title('Hammond - Project 2')
    window.geometry('550x180')

    widgets = GUI(window)
    window.resizable(False, False)

    window.mainloop()


if __name__ == '__main__':
    main()
