from common.conftest import AppStart
from page.base_page import BasePage
from steps.login_action import AllMethod


class TestAccountLogin:
    driver = AppStart.start()
    AllMethod(driver).login_step()

