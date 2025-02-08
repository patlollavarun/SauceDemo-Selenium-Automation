# SauceDemo-Selenium-Automation
A simple Selenium WebDriver script to automate testing of the Sauce Demo website (https://www.saucedemo.com).

## What it does
This script automates the following workflow:
1. Logs into the Sauce Demo website
2. Adds a product to the cart
3. Completes the checkout process
4. Verifies the order confirmation

## Setup
1. Install Python 3.x from [python.org]
2. Install required packages:
pip install selenium
3. Install Chrome WebDriver:
   - Download ChromeDriver from [here](https://sites.google.com/chromium.org/driver/)
   - Add it to your system PATH

## Running the Script
1. Save the script as sauce_demo.py
2. Run it using Python:
python sauce_demo.py

## Structure
The script uses:
- Selenium WebDriver for browser automation
- Chrome browser for testing
- Basic assertions for verification

## Notes
- Make sure Chrome browser is installed
- Includes basic wait times to handle page loading
