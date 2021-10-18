import pytest
from selenium import webdriver

from TestData.formdata import homeformdata


def pytest_addoption(parser):
    parser.addoption("--browser_name", action ="store", default = "chrome")

@pytest.fixture(scope="class")
def setup(request):
    browsername=request.config.getoption("browser_name")

    if browsername == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
    elif browsername == "edge":
        driver = webdriver.Edge(executable_path="C:\\edgedriver_win64\\msedgedriver.exe")
    driver.maximize_window()
    baseurl = "https://rahulshettyacademy.com/angularpractice/"
    driver.get(baseurl)
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture(params= homeformdata.formdatavalue)
def form(request):
    return request.param
