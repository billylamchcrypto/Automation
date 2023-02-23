from page.login_page import LoginPage
from page.base_page import BasePage


class AllMethod(object):
    def __init__(self, driver):
        self.driver = driver

    def login_step(self):
        driver = LoginPage(self.driver)
        driver.login_account()
        driver.click_email()
        driver.enter_email()
        driver.email_ctn()




