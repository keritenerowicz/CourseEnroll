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

    # add term argument
    def __init__(self):
        super(Window, self).__init__()
        #self.term = term
        self.timeout = 180
        self.timeoutUser = 86400
        self.loaded = False
        self.toaster = ToastNotifier()
        self.login()
        self.term()
        self.checkTime()
        self.waitEnrOpen()


    """
    Open Student Center webpage and wait for user to log in.
    """
    def login(self):
        self.get('https://studentcenter.cornell.edu')

        #actions = ActionChains(self)
        #actions.send_keys('netID' + Keys.TAB + 'password' + Keys.ENTER)
        #actions.perform()
        self.toaster.show_toast('Login',
                                'Please log in through the opened Chrome window.',
                                icon_path = 'images\logo.ico',
                                duration = 10)
        while True:
            try:
                self.switch_to_frame('ptifrmtgtframe')
                break
            except:
                continue
        self.click('DERIVED_SSS_SCR_SSS_LINK_ANCHOR3', self.timeout) # clicks 'Enroll' in sidebar


    """
    Pause program while user selects term.
    """
    def term(self):
        if self.elementPresent('win0divSSR_DUMMY_RECV1GP$0'): # 'Select a term then select Continue.'
            # alert user to select the term
            self.toaster.show_toast('Select Term',
                                    'Please select the term in the opened Chrome window, then click "Continue".',
                                    icon_path = 'images\logo.ico',
                                    duration = 10)

            while not self.elementPresent('DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$'): # 'Enter' class nbr button
                continue
        else:
            if self.term == 'Fall':
                pass
            elif self.term == 'Spring':
                pass
            elif self.term == 'Summer':
                pass
            elif self.term == 'Winter':
                pass

    """
    Pause program until 7 am EST.
    """
    def checkTime(self):
        now = datetime.now()
        while(now.strftime("%H:%M:%S") != '07:00:00'):
            now = datetime.now()
            print(now.strftime("%H:%M:%S"))


    """
    Check page until enrollment is open, then attempt an initial enroll.
    """
    def waitEnrOpen(self):
        self.click('DERIVED_REGFRM1_LINK_ADD_ENRL$82$', self.timeoutUser) # 'Proceed to Step 2 of 3' button
        self.pageLoaded()
        while self.elementPresentWait('DERIVED_SASSMSG_ERROR_TEXT$0', .05): # 'You do not have a valid enrollment appointment at this time.'
            self.pageLoaded()
            self.click('DERIVED_REGFRM1_LINK_ADD_ENRL$82$', self.timeoutUser) # 'Proceed to Step 2 of 3' button
            self.pageLoaded()
            if self.elementPresentWait('DERIVED_REGFRM1_SSR_PB_SUBMIT', .02): # 'Finish Enrolling' button
                break
        self.click('DERIVED_REGFRM1_SSR_PB_SUBMIT', self.timeout) # 'Finish Enrolling' button
        self.click('DERIVED_REGFRM1_SSR_LINK_STARTOVER', self.timeout) # 'Add Another Class' button


    """
    Click through enrollment screens.
    """
    def enroll(self):

        WebDriverWait(self, self.timeout).until(EC.presence_of_element_located(\
                     (By.ID, 'DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$'))) # 'Enter' class nbr button

        try:
            # checks for 'Class' title in shopping cart to make sure cart not empty
            self.find_element_by_id('SSR_REGFORM_VW$srt6$0')
            # 'Proceed to Step 2 of 3' button, disappears when shopping cart is empty
            self.click('DERIVED_REGFRM1_LINK_ADD_ENRL$82$', self.timeout)
        except TimeoutException:
            self.quit() # close window
            return 'no'
        except:
            self.quit() # close window
            return 'yes'

        try:
            self.click('DERIVED_REGFRM1_SSR_PB_SUBMIT', self.timeout) # 'Finish Enrolling' button
            self.click('DERIVED_REGFRM1_SSR_LINK_STARTOVER', self.timeout) # 'Add Another Class' button
            return 'notYet'
        except:
            self.quit() # close window
            return 'no'


    """
    Wait for element to load then click it.
    """
    def click(self, id, timeout):
        WebDriverWait(self, timeout).until(EC.presence_of_element_located((By.ID, id)))
        self.find_element_by_id(id).click()


    """
    Return boolean saying whether an element exists on a page.
    """
    def elementPresent(self, id):
        try:
            WebDriverWait(self, self.timeout).until(EC.presence_of_element_located((By.ID, id)))
            return True
        except:
            return False


    """
    elementPresent with a 10 second timeout.
    """
    def elementPresentWait(self, id, wait):
        try:
            WebDriverWait(self, wait).until(EC.presence_of_element_located((By.ID, id)))
            return True
        except:
            return False


    """
    Wait for loading image to disappear.
    """
    def pageLoaded(self):
        try:
            while True:
                time.sleep(.5)
                self.find_element_by_xpath('//*[@style="display: none; \position: absolute;\
                right: -205px; z-index: 99991; visibility: visible; top: 196.5px;"]')
        except:
            return
