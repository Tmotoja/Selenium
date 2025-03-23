import wait
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_for_button(driver, element_id):
    locator= ("id", element_id)

    locator_find= EC.visibility_of_element_located(locator)
    wait= WebDriverWait(driver, 10, 0.5)

    return wait.until(locator_find, "Element not found")
driver= webdriver.Chrome()

url= "https://www.saucedemo.com/"

driver.get(url)

try: #login-button
    login_button= wait_for_button(driver, "login-button")

except TimeoutException:
    print("Element not found")
else:
    print("Element found")
finally:
    login_button.click()
    time.sleep(60)