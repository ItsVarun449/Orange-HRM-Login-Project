from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 40)

    # Locators
    email_field = (By.XPATH, '//input[@name="username"]')
    password_field = (By.XPATH, '//input[@name="password"]')
    login_button = (By.XPATH, '//button[text() = " Login "]')
    
    # New locator (after login)
    dashboard_header = (By.XPATH, '//h6[text()="Dashboard"]')

    
    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(self.email_field)).send_keys(email)
    
    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    

    def is_login_successful(self):
        return self.wait.until(EC.visibility_of_element_located(self.dashboard_header)).is_displayed