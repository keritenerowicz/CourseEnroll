from tkinter import *
from PIL import ImageTk, Image

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import courseenroll as ce
import courselist as cl

class App:


    def __init__(self):
        # self.term = self.termBox()
        self.isSuccessful = 'notYet'
        inst = ce.Window() # add term argument for window
        self.enrCheck(inst)
        self.notifyUser()


    """
    Loop through enrollment screens until cart is empty.
    """
    def enrCheck(self, ceInst):
        try:
            while self.isSuccessful == 'notYet':
                # crs.addsDrops() # check for new courses
                self.isSuccessful = ceInst.enroll() # enroll courses currently in cart
        except:
            self.isSuccessful = 'no'


    """
    Notify user that the program is finished.
    """
    def notifyUser(self):
        root = Tk()
        if self.isSuccessful == 'yes':
            root.title('Congratulations!')
            logo = ImageTk.PhotoImage(Image.open('images\logo_success.jpg'))
        else:
            root.title('Error')
            logo = ImageTk.PhotoImage(Image.open('images\logo_failed.jpg'))
        panel = Label(root, image = logo)
        panel.pack(side = "bottom", fill = "both", expand = "yes")
        root.eval('tk::PlaceWindow . center')
        root.attributes("-topmost", True)
        root.mainloop()


if __name__ == "__main__":
    App()
