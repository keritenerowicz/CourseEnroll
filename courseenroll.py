'''
TODO:
 - Fix wating for enrollment to open
 - Fix term selection
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

#from bs4 import BeautifulSoup

class Window(webdriver.Chrome):

    # creates browser window
    def __init__(self):
        super(Window, self).__init__()
        self.timeout = 300
        self.timeoutUser = 86400
        self.timeoutReload = 10
        self.loaded = False
        self.login()
        self.waitEnrOpen()

    # opens Student Center webpage and waits for user to log in
    def login(self):
        self.get('https://studentcenter.cornell.edu')
        while True:
            try:
                self.switch_to_frame('ptifrmtgtframe')
                break
            except:
                continue
        self.click('DERIVED_SSS_SCR_SSS_LINK_ANCHOR3', self.timeout) # click 'Enroll' in sidebar
        '''
        try:
            self.switch_to_frame('ptifrmtgtframe')
            #select futuremost term
        except:
            pass
        '''

    # checks page until enrollment is open, then attempts an initial enroll
    def waitEnrOpen(self):
        while True:
            self.click('DERIVED_REGFRM1_LINK_ADD_ENRL$82$', self.timeoutUser) # 'Proceed to Step 2 of 3' button
            try:
                self.find_element_by_xpath('text about invalid time')
                continue
            except:
                self.click('DERIVED_REGFRM1_SSR_PB_SUBMIT', self.timeout) # 'Finish Enrolling' button
                self.click('DERIVED_REGFRM1_SSR_LINK_STARTOVER', self.timeout) # 'Add Another Class' button

    # clicks through enrollment screens
    def enroll(self):
        try:
            WebDriverWait(self, self.timeout).until(EC.presence_of_element_located((By.ID, 'DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$'))) # 'Enter' class nbr button
            # check for 'Class' title in shopping cart to make sure cart not empty
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

    def clickxpath(self, xpath, timeout):
        WebDriverWait(self, timeout).until(EC.presence_of_element_located((By.XPATH, xpath)))
        self.find_element_by_xpath(xpath).click()

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
