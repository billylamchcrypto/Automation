from appium.webdriver.common.appiumby import By
import yaml
from pathlib import Path


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, value):
        stream = open(str(Path().cwd().parent / 'common/device.yml'), 'r')
        data = yaml.load(stream, Loader=yaml.FullLoader)

        if data['platformName'] == "Android":
            return self.driver.find_element(By.ID, value)
        else:
            return self.driver.find_element(By.IOS_CLASS_CHAIN, value)







