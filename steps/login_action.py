from page.login_page import LoginPage


class AllMethod(object):
    def __init__(self, driver):
        self.driver = driver

    def login_step(self):
        drive = LoginPage(self)
        drive.login_account()
        drive.click_email()
        drive.enter_email()
        drive.email_ctn()




