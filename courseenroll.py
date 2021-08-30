import time
from datetime import datetime

import webbrowser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from tkinter import *
from PIL import ImageTk, Image
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from win10toast import ToastNotifier


class Window(webdriver.Chrome):

    buttonAddAnotherClass = 'DERIVED_REGFRM1_SSR_LINK_STARTOVER'
    buttonEnroll = 'DERIVED_SSS_SCR_SSS_LINK_ANCHOR3'
    buttonEnter = 'DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$'
    buttonFinishEnrolling = 'DERIVED_REGFRM1_SSR_PB_SUBMIT'
    buttonStep2of3 = 'DERIVED_REGFRM1_LINK_ADD_ENRL$82$'

    textClass = 'SSR_REGFORM_VW$srt6$0'
    textSelectTerm = 'win0divSSR_DUMMY_RECV1GP$0'
    textAddClasses = 'DERIVED_REGFRM1_SS_TRANSACT_TITLE'
    textError = 'DERIVED_SASSMSG_ERROR_TEXT$0'


    def __init__(self):
        super(Window, self).__init__()
        self.timeout = 400
        self.timeoutUser = 86400
        self.timeoutLag = .5
        self.timeout0 = .025
        self.startTime = '09:00:00'  # 9 am EST
        self.isSuccessful = 'notYet'
        self.toaster = ToastNotifier()
        self.login()
        #self.term()
        self.checkTime()
        self.waitEnrOpen()
        self.enrCheck()
        self.notify()


    def login(self):
        """Opens Student Center webpage and wait for user to log in."""
        self.get('https://studentcenter.cornell.edu')
        """
        actions = ActionChains(self)
        actions.send_keys('net123' + Keys.TAB + 'password' + Keys.ENTER)
        actions.perform()
        """
        self.toaster.show_toast('Login',
                                   'Please log in through the opened Chrome window.',
                                   icon_path='images\logo.ico',
                                   duration=10)
        while True:
            try:
                self.switch_to_frame('ptifrmtgtframe')
                break
            except:
                continue
        self.click(Window.buttonEnroll, self.timeout)


    def term(self):
        """Pauses program while user selects term."""
        if self.elementPresent(Window.textSelectTerm):
            self.toaster.show_toast('Select Term',
                                    'Please select the term in the opened Chrome window, then click "Continue".',
                                    icon_path='images\logo.ico',
                                    duration=10)
            while not self.elementPresent(Window.buttonEnter):
                continue


    def checkTime(self):
        """Pauses program until start time."""
        now = datetime.now()
        while(now.strftime("%H:%M:%S") != self.startTime):
            now = datetime.now()
            print(now.strftime("%H:%M:%S"))


    def waitEnrOpen(self):
        """Checks cart is not empty, then begin enroll cycle."""
        self.loadPage()
        self.elementPresentWait(Window.textClass, self.timeout)
        while True:
            try:
                self.loadPage()
                self.click(Window.buttonStep2of3, 0)
                continue
            except:
                self.loadPage()
                self.click(Window.buttonFinishEnrolling, self.timeout)
                self.loadPage()
                self.click(Window.buttonAddAnotherClass, self.timeout)
                break

    def enroll(self):
        """Checks that cart is not empty, then continue through enrollment screens."""
        self.loadPage()
        self.elementPresentWait(Window.buttonEnter, self.timeout)

        try:
            self.click(Window.buttonStep2of3, self.timeout)
        except TimeoutException:
            self.quit()
            return 'no'
        except:
            self.quit()
            return 'yes'

        try:
            self.loadPage()
            self.click(Window.buttonFinishEnrolling, self.timeout)
            self.loadPage()
            self.click(Window.buttonAddAnotherClass, self.timeout)
            return 'notYet'
        except:
            self.quit()
            return 'no'


    def enrCheck(self):
        """Loop through enrollment screens until cart is empty."""
        try:
            while self.isSuccessful == 'notYet':
                self.enroll()
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


    def click(self, id, timeout):
        """Waits for element to load then click it."""
        try:
            WebDriverWait(self, timeout).until(EC.presence_of_element_located((By.ID, id)))
            self.find_element_by_id(id).click()
        except:
            WebDriverWait(self, timeout).until(EC.presence_of_element_located((By.ID, id)))
            self.find_element_by_id(id).click()


    def elementPresent(self, id):
        """Returns boolean saying whether an element exists on a page."""
        try:
            WebDriverWait(self, self.timeout).until(EC.presence_of_element_located((By.ID, id)))
            return True
        except:
            return False


    def elementPresentWait(self, id, wait):
        """elementPresent with a given timeout in seconds."""
        try:
            WebDriverWait(self, wait).until(EC.presence_of_element_located((By.ID, id)))
            return True
        except:
            return False


    def loadPage(self):
        """Waits for loading image to disappear."""
        try:
            while True:
                time.sleep(self.timeout0)
                self.find_element_by_xpath('//*[@style="display: none; \position: absolute;\
                right: -205px; z-index: 99991; visibility: visible; top: 196.5px;"]')
        except:
            return


    def windowOpen(self):
        """Returns boolean to check if window is stil open."""
        DISCONNECTED_MSG = 'Unable to evaluate script: disconnected: not connected to DevTools\n'
        if self.get_log('browser')[-1]['message'] == DISCONNECTED_MSG:
            return False
        return True
