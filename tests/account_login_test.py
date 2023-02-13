from common.conftest import AppStart
from page.base_page import BasePage
from steps.login_action import AllMethod


class TestAccountLogin:
    k = AppStart.start()
    k.login_step()

