import pytest
from Pages.homepage import Homepage
from Utilities.teststatus import TestStatus


@pytest.mark.usefixtures("setup")
class Testformshop:

    @pytest.fixture(autouse= True)
    def classsetup(self):
        self.home = Homepage(self.driver)
        self.ts= TestStatus(self.driver)

    def test_formsubmission(self,form):
        self.home.fillform(form["firstname"], form["email"], form["pwd"])
        outputvalue = self.home.validsubmmision()
        self.ts.mark(outputvalue, "Form submission")
        title = self.home.verifytitle()
        self.ts.markfinal("test_formsubmission", title, "Title" )
        self.driver.refresh()

