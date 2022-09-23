import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Valid signup test
def test_01_valid_signup():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://www.facebook.com/")
    title = driver.title
    time.sleep(2)

    wait = WebDriverWait(driver, 10)
    driver.find_element(By.XPATH, "//a[contains(text(),'Create new account')]").click()
    driver.find_element(By.XPATH, "//input[@name='firstname']").send_keys("First")
    driver.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Last")
    driver.find_element(By.XPATH, "//input[@name='reg_email__']").send_keys("abc@mail.com")
    driver.find_element(By.XPATH, "//input[@name='reg_passwd__']").send_keys("pass123")
    month = driver.find_element(By.XPATH, "//select[@id='month']")
    day = driver.find_element(By.XPATH, "//select[@id='day']")
    year = driver.find_element(By.XPATH, "//select[@id='year']")
    print("************" + str(month))
    sel = Select(month)
    sel.select_by_visible_text("Sep")
    sel = Select(day)
    sel.select_by_value("2")
    sel = Select(year)
    sel.select_by_index(24)
    driver.find_element(By.XPATH, "//label[contains(text(),'Male')]").click()

    re_email = driver.find_element(By.XPATH, "//input[@name='reg_email_confirmation__']")
    # wait.until(EC.visibility_of_element_located(re_email))
    # time.sleep(3)
    print(re_email)
    re_email.send_keys("abc@mail.com")
    signup = driver.find_element(By.XPATH, "//button[@name='websubmit']")

    # driver.execute_script("window.scrollTo(0, 1000);")
    signup.click()
    time.sleep(3)


    driver.close()
    driver.quit()
    print("Test Completed!")

# def test_teardown():
#     driver.close()
#     driver.quit()
#     print("Test Completed!")
