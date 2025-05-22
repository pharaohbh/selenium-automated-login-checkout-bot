from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Login Page
url = "https://www.saucedemo.com/"
driver.get(url)

# Enter Username & Password
username_input = driver.find_element(By.ID, "user-name")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("standard_user")  # Test username
password_input.send_keys("secret_sauce")  # Test password
password_input.send_keys(Keys.RETURN)  # Press Enter

# Wait for page to load
time.sleep(3)

# Verify Login Success
if "inventory.html" in driver.current_url:
    print("✅ Login Successful!")
else:
    print("❌ Login Failed!")

# Close the browser
driver.quit()
