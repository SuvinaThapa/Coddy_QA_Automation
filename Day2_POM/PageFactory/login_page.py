from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


USERNAME_FIELD = (By.ID, "username")
PASSWORD_FIELD = (By.ID, "password")
SIGN_IN_BUTTON = (By.XPATH, "//button[text()='Sign in']")
DASHBOARD_LINK = (By.XPATH, "//a[@href='/dashboard']")



def open_login_page(driver):
    driver.get("https://demo.coddypro.com")
    time.sleep(3)


def login(driver, email, password):
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located(USERNAME_FIELD))
    password_field = wait.until(EC.presence_of_element_located(PASSWORD_FIELD))
    login_button = wait.until(EC.element_to_be_clickable(SIGN_IN_BUTTON))

    username_field.send_keys(email)
    password_field.send_keys(password)
    login_button.click()


def verify_login_success(driver):
    try:
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located(DASHBOARD_LINK))
        print("Login Successful!")
    except:

        print("Login Failed - current URL was:", driver.current_url)