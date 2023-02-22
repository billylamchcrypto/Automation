import yaml
from appium import webdriver
from pathlib import Path
import time


class AppStart:

    @classmethod
    def start(cls):
        stream = open(str(Path().cwd().parent / 'common/device.yml'), 'r')
        data = yaml.load(stream, Loader=yaml.FullLoader)

        desired_caps = {}
        desired_caps['platformName'] = data['platformName']
        desired_caps['platformVersion'] = str(data['platformVersion'])
        desired_caps['deviceName'] = data['deviceName']
        desired_caps['appPackage'] = data['appPackage']
        desired_caps['automationName'] = data['automationName']
        desired_caps['app'] = data['app']
        desired_caps['unicodeKeyboard'] = data['unicodeKeyboard']
        desired_caps['resetKeyboard'] = data['resetKeyboard']
        # desired_caps['locale'] = data['locale']

        cls.driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', desired_caps)
        cls.driver.implicitly_wait(20)
        time.sleep(3)
        return cls.driver

    @classmethod
    def quit(cls):
        cls.driver.quit()
