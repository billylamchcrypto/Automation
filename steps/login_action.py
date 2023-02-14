from page.login_page import LoginPage


class AllMethod(object):
    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)

    def login_step(self):
        self.login_page.login_account()
        self.login_page.click_email()
        self.login_page.enter_email()
        self.login_page.email_ctn()




