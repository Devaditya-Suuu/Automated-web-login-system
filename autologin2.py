from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.chrome.service import Service as ChromeService # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore

# Configure Chrome options
options = Options()
options.add_argument("--ignore-certificate-errors")  # Ignore SSL certificate errors

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=ChromeService(), options=options)

# Navigate to the SonicWall login page
driver.get("https://192.168.192.200/sonicui/7/login/#/")

try:
    # Wait for and fill in the username field
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("4SI24IS064")  # Replace with your actual username

    # Wait for and fill in the password field
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password_field.send_keys("7M3N7011")  # Replace with your actual password

    # Wait for the login button to be clickable using full XPath and scroll into view if necessary
    login_button = WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div/div[4]/div[2]/div"))
    )

    # Scroll to the button and use JavaScript to click it
    driver.execute_script("arguments[0].scrollIntoView(true);", login_button)
    driver.execute_script("arguments[0].click();", login_button)  # Use JavaScript click

    # Wait for login to process (adjust timing as needed)
    WebDriverWait(driver, 5).until(
        EC.title_contains("Dashboard")  # Adjust based on expected title after login
    )
    
    print("Login successful!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()  # Close the browser after completion