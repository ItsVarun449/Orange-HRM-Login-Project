from utilities.driver_setup import get_driver
from pages.login_page import LoginPage


# Step 1: Start browser
driver = get_driver()

# Step 2: Open Website
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Step 3: Create LoginPage Object
login = LoginPage(driver)

# Step 4 : Perform actions
login.enter_email("Admin")
login.enter_password("admin123")
login.click_login()

# Step 5: Assertion
assert login.is_login_successful(), "Login Failed!"
print("Login Successful")
