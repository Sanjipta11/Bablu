from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome()

# Open the demoqa frames page
driver.get('https://demoqa.com/frames')

# Switch to the first iframe and fetch the text
driver.switch_to.frame("frame1")  # Switch to the first iframe by ID
first_frame_text = driver.find_element(By.ID, 'sampleHeading').text
print(f"Text from the first frame: {first_frame_text}")

# Switch back to the main page content
driver.switch_to.default_content()

# Switch to the second iframe and fetch the text
driver.switch_to.frame("frame2")  # Switch to the second iframe by ID
second_frame_text = driver.find_element(By.ID, 'sampleHeading').text
print(f"Text from the second frame: {second_frame_text}")

# Close the browser
driver.quit()
