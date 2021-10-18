import logging

from Base.basemethods import SeleniumDrivers
from Utilities import custom_logging as cl

class Homepage(SeleniumDrivers):
    log = cl.loggingcontent(logging.DEBUG)

    def __init__(self, driver):
        #SeleniumDrivers.__init__(self,driver)
        super(Homepage, self).__init__(driver)
        self.driver = driver

    #locators
    name = "//input[contains(@class, 'form-control') and (@name = 'name')]" #xpath
    email = "[name='email']" #css
    password = "#exampleInputPassword1" #css
    icecheckbox = "exampleCheck1"  #ID
    gender = "exampleFormControlSelect1" # ID
    #empstatus = "//input[@type='radio']" #xpath
    empstatusemployed = "#inlineRadio2"
    empstatusent = "#inlineRadio3"
    datelocation = "[name='bday']" #css
    submitlocation = "[type='submit']" #css
    shoplocation = "Shop"  # link
    successlocation = "//div[contains (@class, 'alert-success')]" #xpath

    def updatefirstname(self, firstname):
        self.sendData(self.name,firstname, "xpath")

    def updateemail(self, email):
        self.sendData(self.email, email, "css")

    def updatepassword(self, password):
        self.sendData(self.password,password, "css")

    def clickicecheckbox(self):
        self.clickElement(self.icecheckbox)

    def clickgenderdropdown(self):
        self.getdropwn(self.gender, "Female")

    def clickempstatus(self):
        self.clickElement(self.empstatusemployed, "css")

    def checkenabled(self):
        enable=self.iselementenabled(self.empstatusent, "css")
        return enable

    def clickdate(self):
        self.clickElement(self.datelocation)

    def updateday(self, date):
        self.sendData(self.datelocation, date, "css")

    def updatemonth(self, month):
        self.sendData(self.datelocation, month, "css")

    def updateyear(self, year):
        self.sendData(self.datelocation, year, "css")

    def clickSubmit(self):
        self.clickElement(self.submitlocation, "css")

    def successmsg(self):
        message= self.getElement(self.successlocation, "xpath").text
        return message
        #if "Success" in message:
            #return True
        #else:
            #return False

    def verifycheckboxpresent(self):
        present=self.iselementpresent(self.name, "xpath")
        return present

    def fillform(self, firstname, email, password):
        self.updatefirstname(firstname)
        self.updateemail(email)
        self.updatepassword(password)
        self.clickicecheckbox()
        self.clickgenderdropdown()
        self.clickempstatus()
        self.clickdate()
        self.updateday(15)
        self.updatemonth(10)
        self.updateyear(2021)
        self.clickSubmit()

    def validsubmmision(self):
        message = self.successmsg()
        if "Success" in message:
            return True
        else:
            return False

    def verifytitle(self):
        title = self.getTitle()
        if title == "ProtoCommercehj":
            return True
        else:
            return False




