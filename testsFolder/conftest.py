import pytest
from selenium import webdriver


@pytest.fixture()
def getDriver(request):
    broswer = request.config.getoption("--browser_name")
    if broswer == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Vikas_Data\\chromedriver_win32\\chromedriver.exe")
    elif broswer == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\Vikas_Data\\geckodriver-v0.26.0-win64\\geckodriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
