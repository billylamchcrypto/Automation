from page.login_page import LoginPage


class AllMethod(LoginPage):

    def login_step(self):
        self.login_account()
        self.click_email()
        self.enter_email()
        self.email_ctn()
