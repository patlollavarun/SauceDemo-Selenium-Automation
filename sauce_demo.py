from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()  # Ensure chromedriver is installed and in PATH
driver.maximize_window()

# Navigate to Sauce Demo
driver.get("https://www.saucedemo.com")
print("Page Title:", driver.title)

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)  # Wait for page to load

# Add third product to cart
products = driver.find_elements(By.CLASS_NAME, "inventory_item")
products[2].find_element(By.CLASS_NAME, "btn_inventory").click()
time.sleep(2)

# Go to Cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# Verify product in cart
cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
assert len(cart_items) > 0, "Cart is empty!"
print("Product successfully added to cart")

# Proceed to Checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(2)

# Enter checkout details
driver.find_element(By.ID, "first-name").send_keys("Test")
driver.find_element(By.ID, "last-name").send_keys("User")
driver.find_element(By.ID, "postal-code").send_keys("12345")
driver.find_element(By.ID, "continue").click()
time.sleep(2)

# Finish order
driver.find_element(By.ID, "finish").click()
time.sleep(2)

# Verify success message
success_message = driver.find_element(By.CLASS_NAME, "complete-header").text
assert success_message == "THANK YOU FOR YOUR ORDER", "Order not completed!"
print("Order placed successfully!")


# Close Browser
driver.quit()