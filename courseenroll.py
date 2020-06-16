'''
TODO:
 - Automate term seleciton
 - Fix adds() and drops()
'''


import time
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from tkinter import *
from tkinter import messagebox


class Window(webdriver.Chrome):


    # creates browser window
    # add term argument
    def __init__(self):
        super(Window, self).__init__()
        #self.term = term
        self.timeout = 300
        self.timeoutUser = 86400
        self.timeoutReload = 10
        self.loaded = False
        self.login()
        self.term()
        self.waitEnrOpen()
        self.enroll()


    # opens Student Center webpage and waits for user to log in
    def login(self):
        self.get('https://studentcenter.cornell.edu')
        while True:
            try:
                self.switch_to_frame('ptifrmtgtframe')
                break
            except:
                continue
        self.click('DERIVED_SSS_SCR_SSS_LINK_ANCHOR3', self.timeout) # clicks 'Enroll' in sidebar


    # stops program while user selects term
    def term(self):
        if self.elementPresent('win0divSSR_DUMMY_RECV1GP$0'): # 'Select a term then select Continue.'
            # alert user to select the term
            root = Tk()
            root.title('Select Term')
            Label(root, text = '\n      Please select the term in the opened Chrome window, then click "Continue".      \n').grid()
            root.eval('tk::PlaceWindow . center')
            root.attributes("-topmost", True)
            root.mainloop()
            while not self.elementPresent('DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$'): # 'Enter' class nbr button
                continue
                '''
                if self.term == 'Fall':
                    pass
                elif self.term == 'Spring':
                    pass
                elif self.term == 'Summer':
                    pass
                elif self.term == 'Winter':
                    pass
                '''


    # checks page until enrollment is open, then attempts an initial enroll
    def waitEnrOpen(self):
        self.click('DERIVED_REGFRM1_LINK_ADD_ENRL$82$', self.timeoutUser) # 'Proceed to Step 2 of 3' button

        self.elementPresent('DERIVED_REGFRM1_SS_TRANSACT_TITLE')
        while self.elementPresentNoWait('DERIVED_SASSMSG_ERROR_TEXT$0'): #'You do not have a valid enrollment appointment at this time.'
            time.sleep(.1)
            self.click('DERIVED_REGFRM1_LINK_ADD_ENRL$82$', self.timeoutUser) # 'Proceed to Step 2 of 3' button
            if self.elementPresent('DERIVED_REGFRM1_SSR_PB_SUBMIT'): # 'Finish Enrolling' button
                break
        self.click('DERIVED_REGFRM1_SSR_PB_SUBMIT', self.timeout) # 'Finish Enrolling' button
        self.click('DERIVED_REGFRM1_SSR_LINK_STARTOVER', self.timeout) # 'Add Another Class' button


    # clicks through enrollment screens
    def enroll(self):
        while True:
            try:
                WebDriverWait(self, self.timeout).until(EC.presence_of_element_located((By.ID, 'DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$'))) # 'Enter' class nbr button
                # checks for 'Class' title in shopping cart to make sure cart not empty
                self.find_element_by_id('SSR_REGFORM_VW$srt6$0')
                # this button disappears when shopping cart is empty, goes to generic exception
                self.click('DERIVED_REGFRM1_LINK_ADD_ENRL$82$', self.timeout) # 'Proceed to Step 2 of 3' button
                self.click('DERIVED_REGFRM1_SSR_PB_SUBMIT', self.timeout) # 'Finish Enrolling' button
                self.click('DERIVED_REGFRM1_SSR_LINK_STARTOVER', self.timeout) # 'Add Another Class' button
            except:
                self.quit() # close window
                return


    # waits for element to load then clicks it
    def click(self, id, timeout):
        WebDriverWait(self, timeout).until(EC.presence_of_element_located((By.ID, id)))
        self.find_element_by_id(id).click()


    # returns boolean saying whether an element exists on a page
    def elementPresent(self, id):
        try:
            WebDriverWait(self, self.timeout).until(EC.presence_of_element_located((By.ID, id)))
            return True
        except:
            return False

    # elementPresent without the timeout
    def elementPresentNoWait(self, id):
        try:
            self.find_element_by_id(id)
            return True
        except:
            return False


    # adds new courses through Student Center
    def adds(self, courseNum):
        self.click('DERIVED_REGFRM1_CLASS_NBR', self.timeout)
        actions = ActionChains(driver)
        actions.send_keys(courseNum + Keys.ENTER)
        actions.perform()
        # if discussion
            # if multi discussion
        # if lab
            # if multi lab
        self.click('DERIVED_CLS_DTL_WAIT_LIST_OKAY$125$', self.timeout)
        self.click('DERIVED_CLS_DTL_NEXT_PB$280$', self.timeout)


    # drops deleted courses through Student Center
    def drops(self, courseNum):
        #beautifulsoup to find course's #th place in list
        #beautifulsoup to find #th trash icon
        #clickxpath('', self.timeout)
        pass
