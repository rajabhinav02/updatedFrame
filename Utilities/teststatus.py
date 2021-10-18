import logging

from Base.basemethods import SeleniumDrivers
from Utilities import custom_logging as cl


class TestStatus(SeleniumDrivers):
    log = cl.loggingcontent(logging.DEBUG)
    #resultlist = []
    def __init__(self, driver):
        super(TestStatus, self).__init__(driver)
        self.resultlist = []

    def setTestStatus(self, result, resultmessage):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.log.info("##VERIFICATION SUCCESSFUL " +resultmessage)
                else:
                    self.resultlist.append("FAIL")
                    self.getScreenshot(resultmessage)
                    self.log.info("###VERIFICATION FAILED " +resultmessage)
            else:
                self.resultlist.append("FAIL")
                self.getScreenshot(resultmessage)
                self.log.error("###VERIFICATION FAILED " + resultmessage)
        except:
            self.resultlist.append("FAIL")
            self.getScreenshot(resultmessage)
            self.log.error("###VERIFICATION FAILED " + resultmessage)

    def mark(self, result, resultmessage):
        self.setTestStatus(result, resultmessage)

    def markfinal(self, testname, result, resultmessage):
        self.setTestStatus(result, resultmessage)
        if "FAIL" in self.resultlist:
            self.log.error(testname + " failed "  )
            self.resultlist.clear()
            assert True == False

        else:
            self.log.info(testname + " passed")
            self.resultlist.clear()
            assert True == True







