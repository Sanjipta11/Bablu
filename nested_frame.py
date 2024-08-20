from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome()

# Open the demoqa nested frames page
driver.get('https://demoqa.com/nestedframes')


# Switch to the parent frame by using its name or index
driver.switch_to.frame(driver.find_element(By.CSS_SELECTOR, "iframe#frame1"))

# Fetch and print the text from the parent frame
parent_frame_text = driver.find_element(By.TAG_NAME, 'body').text
print(f"Text from the parent frame: {parent_frame_text}")

# Switch to the child frame inside the parent frame
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))

# Fetch and print the text from the child frame
child_frame_text = driver.find_element(By.TAG_NAME, 'p').text
print(f"Text from the child frame: {child_frame_text}")

# Switch back to the main page content
driver.switch_to.default_content()

# Close the browser
driver.quit()
