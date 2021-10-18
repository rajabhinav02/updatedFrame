import pytest

from Pages.homepage import Homepage


@pytest.mark.usefixtures("setup")
class TestCase:

    @pytest.fixture(autouse=True)
    def classlevel(self):
        self.home = Homepage(self.driver)

    def test_formfill(self, form):
        self.home.updatefirstname(form["firstname"])
        self.home.updateemail(form["email"])
        self.home.updatepassword(form["pwd"])
        self.home.clickicecheckbox()
        self.home.clickgenderdropdown()
        self.home.clickempstatus()
        value=self.home.checkenabled()
        assert value==False
        #result1=self.home.verifycheckboxpresent()
        #assert result1 == True
        self.home.clickdate()
        self.home.updateday("10")
        self.home.updatemonth("09")
        self.home.updateyear("2021")
        self.home.clickSubmit()
        result2 =self.home.successmsg()
        assert result2 == True
        self.driver.refresh()