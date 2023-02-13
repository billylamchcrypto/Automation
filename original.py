from appium import webdriver
from appium.webdriver.common.appiumby import By
import time


desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = "emulator-5554"
desired_caps['appPackage'] = 'co.mona.android.staging'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['app'] = '/Users/billylam/Downloads/37406.apk'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
time.sleep(2)
driver.find_element(By.resource-id, 'co.mona.android.staging:id/rb9').click()
driver.find_element(By.resource-id, 'co.mona.android.staging:id/rb8').click()
driver.find_element(By.resource-id, 'co.mona.android.staging:id/rb7').click()
driver.find_element(By.resource-id, 'co.mona.android.staging:id/rb6').click()
driver.find_element(By.resource-id, 'co.mona.android.staging:id/rb5').click()
driver.find_element(By.resource-id, 'co.mona.android.staging:id/rb4').click()
time.sleep(5)


driver.quit()

