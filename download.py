import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome()

# Open the demoqa upload-download page
driver.get('https://demoqa.com/upload-download')

# Locate the download button and click it to download the file
download_button = driver.find_element(By.ID, 'downloadButton')
download_button.click()

# Wait for the download to complete (adjust the time as needed)
time.sleep(5)  # Adjust the sleep time based on download speed

# Close the browser
driver.quit()
