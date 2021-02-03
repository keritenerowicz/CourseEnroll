from datetime import datetime
import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from win10toast import ToastNotifier


class Window(webdriver.Chrome):

    buttonAddAnotherClass = 'DERIVED_REGFRM1_SSR_LINK_STARTOVER'
    buttonEnroll = 'DERIVED_SSS_SCR_SSS_LINK_ANCHOR3'
    buttonEnter = 'DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$'
    buttonFinishEnrolling = 'DERIVED_REGFRM1_SSR_PB_SUBMIT'
    buttonStep2of3 = 'DERIVED_REGFRM1_LINK_ADD_ENRL$82$'

    textClass = 'SSR_REGFORM_VW$srt6$0'
    textNoValidEnrollmentTime = 'DERIVED_SASSMSG_ERROR_TEXT$0'
    textSelectTerm = 'win0divSSR_DUMMY_RECV1GP$0'

    def __init__(self):
        super(Window, self).__init__()
        self.timeout = 500
        self.timeoutUser = 86400
        self.loaded = False
        self.startTime = '08:00:00'  # 8 am EST
        self.toaster = ToastNotifier()
        self.login()
        self.term()
        self.checkTime()
        self.waitEnrOpen()

    def login(self):
        """Opens Student Center webpage and wait for user to log in."""

        self.get('https://studentcenter.cornell.edu')

        actions = ActionChains(self)
        #actions.send_keys('un' + Keys.TAB + 'pw' + Keys.ENTER)
        actions.perform()
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

        try:
            self.loadPage()
            self.find_element_by_id(Window.textClass)
        except:
            return
        if self.windowOpen():
            self.firstCycle()

    def firstCycle(self):
        """Attempts cycle until time period opens, the finish first cycle through enrollment screens."""

        self.loadPage()
        self.click(Window.buttonStep2of3, self.timeoutUser)
        self.loadPage()
        while self.elementPresentWait(Window.textNoValidEnrollmentTime, .05):
            self.click(Window.buttonStep2of3, self.timeoutUser)
            self.loadPage()
            if self.elementPresentWait(Window.buttonFinishEnrolling, .25):
                break
        self.click(Window.buttonFinishEnrolling, self.timeout)
        self.loadPage()
        self.click(Window.buttonAddAnotherClass, self.timeout)

    def enroll(self):
        """Checks that cart is not empty, then continue through enrollment screens."""

        self.loadPage()
        WebDriverWait(self, self.timeout).until(EC.presence_of_element_located(
                     (By.ID, Window.buttonEnter)))

        try:
            self.find_element_by_id(Window.textClass)
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

    def click(self, id, timeout):
        """Waits for element to load then click it."""

        WebDriverWait(self, timeout).until(
            EC.presence_of_element_located((By.ID, id)))
        self.find_element_by_id(id).click()

    def elementPresent(self, id):
        """Returns boolean saying whether an element exists on a page."""

        try:
            WebDriverWait(self, self.timeout).until(
                EC.presence_of_element_located((By.ID, id)))
            return True
        except:
            return False

    def elementPresentWait(self, id, wait):
        """elementPresent with a given timeout in seconds."""

        try:
            WebDriverWait(self, wait).until(
                EC.presence_of_element_located((By.ID, id)))
            return True
        except:
            return False

    def loadPage(self):
        """Waits for loading image to disappear."""

        try:
            while True:
                time.sleep(.025)
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
