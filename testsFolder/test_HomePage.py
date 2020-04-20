import pytest
from selenium.webdriver.support.select import Select

from Utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage
from testData.HomePageData import HomePageData


class Test_HomePage(BaseClass):

    def test_FormSubmission(self, useTestData):
        log = self.log()
        homePage = HomePage(self.driver)
        log.info("Enter Name = " + useTestData["name"])
        homePage.EnterName(useTestData["name"])
        self.driver.find_element_by_id("exampleCheck1").click()

        # select calss to select dropdown
        dropDown = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        log.info("Select Gender = " + useTestData["gender"])
        dropDown.select_by_visible_text(useTestData["gender"])

    @pytest.fixture(params=[HomePageData.getTestData("TC1"), HomePageData.getTestData("TC2")])
    def useTestData(self, request):
        return request.param
