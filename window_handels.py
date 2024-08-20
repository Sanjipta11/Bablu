from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver (replace 'chromedriver' with the path to your driver)
driver = webdriver.Chrome()

# Open the demoqa browser windows page
driver.get('https://demoqa.com/browser-windows')

# Handle New Tab
# new_tab_button = driver.find_element(By.ID, 'tabButton')
# new_tab_button.click()
#
# # Switch to the new tab
# driver.switch_to.window(driver.window_handles[1])
#
# # Fetch and print the text from the new tab
# new_tab_text = driver.find_element(By.ID, 'sampleHeading').text
# print(f"Text from the new tab: {new_tab_text}")
#
# # Close the new tab and switch back to the original window
# driver.close()
# driver.switch_to.window(driver.window_handles[0])

# # Handle New Window
new_window_button = driver.find_element(By.ID, 'windowButton')
new_window_button.click()
#
# # Switch to the new window
driver.switch_to.window(driver.window_handles[1])

# # Fetch and print the text from the new window
new_window_text = driver.find_element(By.ID, 'sampleHeading').text
print(f"Text from the new window: {new_window_text}")
#
# # Close the new window and switch back to the original window
# driver.close()
# driver.switch_to.window(driver.window_handles[0])
#
# # Handle New Window Message
# new_window_message_button = driver.find_element(By.ID, 'messageWindowButton')
# new_window_message_button.click()
#
# # Switch to the new window
# driver.switch_to.window(driver.window_handles[1])
#
# # Fetch and print the text from the new window message
# new_window_message_text = driver.find_element(By.TAG_NAME, 'body').text
# print(f"Text from the new window message: {new_window_message_text}")
#
# # Close the new window message and switch back to the original window
# driver.close()
# driver.switch_to.window(driver.window_handles[0])

# Close the browser
driver.quit()
