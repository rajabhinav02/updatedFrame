import logging
import os
import time
from traceback import print_stack

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import Utilities.custom_logging as cl

class SeleniumDrivers:
    log = cl.loggingcontent(logging.DEBUG)
    def __init__(self, driver):
        self.driver = driver

    def getScreenshot(self, resultmessage):
        filename = resultmessage + "." +str(round(time.time()*1000)) +".png"
        screenshotDirectory = "../Screenshots/"
        relativeFilename = screenshotDirectory + filename
        currentDirectory = os.path.dirname(__file__)
        destinationFileName = os.path.join(currentDirectory, relativeFilename)
        destinationDirectory = os.path.join(currentDirectory, screenshotDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
            self.driver.save_screenshot(destinationFileName)
            self.log.info("Screenshot save to the directory: " +destinationFileName)
        except:
            self.log.error("Screenshot not saved")
            print_stack()

    def getBytype(self, locatortype):
        locatortype = locatortype.lower()

        if locatortype == "id":
            return By.ID
        elif locatortype == "xpath":
            return By.XPATH
        elif locatortype == "css":
            return By.CSS_SELECTOR
        elif locatortype == "class":
            return By.CLASS_NAME
        elif locatortype == "link":
            return By.LINK_TEXT
        elif locatortype == "name":
            return By.NAME
        else:
            self.log.info("element with locatortype "+locatortype +"not found")

    def getElement(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            byType = self.getBytype(locatortype)
            element = self.driver.find_element(byType, locator)
            self.log.info("element with locator type" + locatortype + "and locator" + locator + "found")
        except:
            self.log.info("element with locator type" + locatortype + "and locator" + locator + "not found")
            print_stack()
        return element

    def getElements(self, locator, locatortype="id"):
        try:
            locatortype = locatortype.lower()
            byType = self.getBytype(locatortype)
            elementlist = self.driver.find_elements(byType, locator)
            self.log.info("elements with locator type" + locatortype + "and locator" + locator + "found")
        except:
            self.log.info("elements with locator type" + locatortype + "and locator" + locator + "not found")
        return elementlist


    def clickElement(self, locator, locatortype= "id"):
        try:
            locatortype = locatortype.lower()
            element=self.getElement(locator, locatortype)
            element.click()
            self.log.info("element with locator type" + locatortype + "and locator" + locator + "clicked")
        except:
            self.log.info("element with locator type" + locatortype + "and locator" + locator + "not clicked")
            print_stack()

    def sendData(self, locator, data, locatortype="id"):
        try:
            locatortype= locatortype.lower()
            element = self.getElement(locator, locatortype)
            element.send_keys(data)
            self.log.info("data " +data +"send to element with locator type" + locatortype + "and locator" + locator)
        except:
            self.log.info("data NOT send to element with locator type" + locatortype + "and locator" + locator)
            print_stack()

    def iselementpresent(self, locator, locatortype="id"):

        locatortype= locatortype.lower()
        elementlist = self.getElements(locator, locatortype)
        if len(elementlist) > 0:
            self.log.info("element with locator type" + locatortype + "and locator" + locator + "is present")
            return True
        else:
            self.log.info("element with locator type" + locatortype + "and locator" + locator + "is not present")
            return False

    def waiting(self, locator, time, locatortype= "id"):
        try:
            locatortype = locatortype.lower()
            byType = self.getBytype(locatortype)
            wait = WebDriverWait(self.driver, time)
            wait.until(EC.presence_of_element_located((byType, locator)))
            self.log.info("element with locator type" + locatortype + "and locator" + locator + "is now present")
        except:
            self.log.info("element with locator type" + locatortype + "and locator" + locator + "is not present")
            print_stack()

    def getdropwn(self, locator, text, locatortype="id"):
        locatortype = locatortype.lower()
        byType = self.getBytype(locatortype)
        select = Select(self.driver.find_element(byType, locator))
        select.select_by_visible_text(text)

    def iselementenabled(self, locator, locatortype= "id"):
        try:
            locatortype = locatortype.lower()
            element=self.getElement(locator, locatortype)
            if element.is_enabled == True:
                self.log.info("element with locator type " + locatortype + "and locator" +locator +"is enabled")
                return True
            else:
                self.log.info("element with locator type " + locatortype + "and locator" +locator +"is disabled")
                return False
        except:
            self.log.info("element for which enabled is checked is not found")

    def clickallradio(self, locator, locatortype):
        try:
            locatortype = locatortype.lower()
            elementlist = self.getElements()
            for element in elementlist:
                element.click()
                time.sleep(2)
            self.log.info("all elements with locatortype " +locatortype + "and locator" +locator + "have been clicked")
        except:
            self.log.info("no elements with locatortype " +locatortype +"and locator" +locator +"found")

    def getTitle(self):
        title = self.driver.title
        return title









