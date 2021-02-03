from tkinter import *
from PIL import ImageTk, Image
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import courseenroll as ce


class App():

    def __init__(self):
        self.isSuccessful = 'notYet'
        inst = ce.Window()
        self.enrCheck(inst)
        self.notify()

    def enrCheck(self, ceInst):
        """Loop through enrollment screens until cart is empty."""

        try:
            while self.isSuccessful == 'notYet':
                self.isSuccessful = ceInst.enroll()
        except:
            self.isSuccessful = 'no'

    def notify(self):
        """Notify user that the program is finished."""

        self.root = Tk()
        if self.isSuccessful == 'yes':
            self.root.title('Congratulations!')
            logo = ImageTk.PhotoImage(Image.open('images\logo_success.jpg'))
        else:
            self.root.title('Error')
            logo = ImageTk.PhotoImage(Image.open('images\logo_failed.jpg'))
        panel = Label(self.root, image=logo)
        panel.pack(side="bottom", fill="both", expand="yes")
        self.root.eval('tk::PlaceWindow . center')
        self.root.lift()
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        self.root.mainloop()


if __name__ == "__main__":
    App()
