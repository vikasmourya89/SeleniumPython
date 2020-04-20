from selenium.webdriver.common.by import By


class CheckoutPage:
    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    successBtn = (By.XPATH, "//button[@class='btn btn-success']")

    def __init__(self, driver):
        self.driver = driver

    def getcardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getSuccessButton(self):
        return self.driver.find_element(*CheckoutPage.successBtn)
