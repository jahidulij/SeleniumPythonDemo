import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin():

    @pytest.fixture
    def test_setup(self):
        global driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.close()
        self.driver.quit()
        print("Test Completed!")

    # Valid login test
    def test_01_valid_login(self, test_setup):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        title = self.driver.title
        time.sleep(2)
        menu_button = self.driver.find_element(By.ID, "react-burger-menu-btn")
        menu_button.click()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "logout_sidebar_link")))

        logout = self.driver.find_element(By.ID, "logout_sidebar_link").click()

    # Invalid username or password
    def test_02_invalid_login(self, test_setup):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce1")
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text
        time.sleep(3)
        print(error_message)

    # Empty username
    def test_03_invalid_login(self, test_setup):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text
        time.sleep(3)
        print(error_message)

        # Empty password
    def test_04_invalid_login(self, test_setup):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").clear()
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3").text
        time.sleep(3)
        print(error_message)

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test Completed!")

