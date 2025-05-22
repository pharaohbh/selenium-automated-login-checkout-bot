from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open SauceDemo
driver.get("https://www.saucedemo.com/")

# Step 1: Log in
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)  # Wait for page load

# Step 2: Add item to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)  # Wait for item to be added

# Step 3: Go to Cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(1)

# Step 4: Proceed to Checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(1)

# Step 5: Fill in Checkout Details
driver.find_element(By.ID, "first-name").send_keys("John")
driver.find_element(By.ID, "last-name").send_keys("Doe")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()
time.sleep(1)

# Step 6: Verify Order Summary
summary = driver.find_element(By.CLASS_NAME, "summary_total_label").text
print("🛒 Order Total:", summary)

# Step 7: Finish Checkout
driver.find_element(By.ID, "finish").click()
time.sleep(2)

# Step 8: Verify Success Message
success_msg = driver.find_element(By.CLASS_NAME, "complete-header").text
if "THANK YOU" in success_msg.upper():
    print("✅ Checkout Successful!")
else:
    print("❌ Checkout Failed!")

# Close Browser
driver.quit()
