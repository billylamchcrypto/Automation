from page.base_page import BasePage


class LoginPage(BasePage):
    loginButton = "l86"
    emailBox = "102"
    emailCtn = "qir"

    def login_account(self):
        return self.find_element(self.loginButton).click()

    def click_email(self):
        return self.find_element(self.emailBox).click()

    def enter_email(self):
        return self.find_element(self.emailBox).send_keys("billy.lam+td35@crypto.com")

    def email_ctn(self):
        return self.find_element(self.emailCtn).click()