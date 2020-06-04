'''
TODO:
 - Eliminate use of shell
'''

from tkinter import *
from PIL import ImageTk, Image

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import courseenroll as ce
import courselist as cl

class App:

    def __init__(self):
        self.done = False
        crs = cl.CourseList()
        inst = ce.Window()
        self.enrCheck()
        self.notifyUser()

    # loops through enrollment screens until cart is empty
    def enrCheck(self):
        while not self.done:
            try:
                crs.addsDrops() # check for new courses
                inst.enroll() # enroll courses currently in cart
                self.done = True
            except:
                return

    # notify user that the program is finished
    def notifyUser(self):
        root = Tk()
        if self.done:
            root.title('Congratulations!')
            logo = ImageTk.PhotoImage(Image.open('images\logo.jpg'))
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
