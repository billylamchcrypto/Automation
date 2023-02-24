from common.conftest import AppStart
from steps.login_action import AllMethod


class TestAccountLogin:
    driver = AppStart.start()
    AllMethod(driver).login_step()

