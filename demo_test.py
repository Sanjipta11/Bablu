# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# # Initialize the WebDriver
# driver = webdriver.Chrome()
#
# try:
#     # Navigate to Naukri login page
#     driver.get("https://www.naukri.com/nlogin/login?URL=http://www.naukri.com/mnjuser/profile")
#     driver.maximize_window()
#
#     # Log in to Naukri
#     driver.find_element(By.ID, "usernameField").send_keys("your_email@example.com")
#     driver.find_element(By.ID, "passwordField").send_keys("your_password")
#     driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
#
#     # Wait for the login to complete
#     time.sleep(5)
#
#     # Navigate to the profile section
#     driver.get("https://www.naukri.com/mnjuser/profile")
#     time.sleep(5)
#
#     # Find the profile image section and click to update
#     profile_img = driver.find_element(By.XPATH, "//div[@class='nI-gNb-profile-image__upload']")
#     profile_img.click()
#     time.sleep(3)
#
#     # Upload the new profile image
#     file_input = driver.find_element(By.XPATH, "//input[@type='file']")
#     file_input.send_keys(r'C:\path\to\your\profile_image.jpg')  # Replace with your file path
#     time.sleep(5)
#
#     # Confirm the upload (if required)
#     # If there's a submit button or any confirmation step, handle it here.
#     # Example:
#     # driver.find_element(By.XPATH, "//button[text()='Save']").click()
#
#     print("Profile image updated successfully!")
#
# finally:
#     # Close the browser
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/nlogin/login")
driver.maximize_window()

# Login to Naukri
driver.find_element(By.ID, "usernameField").send_keys("sanjipt330@gmail.com")
driver.find_element(By.ID, "passwordField").send_keys("Sanjipt@2024")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "#loginForm > div:nth-child(2) > div.action.row.mb0 > div > button.waves-effect.waves-light.btn-large.btn-block.btn-bold.blue-btn.textTransform").click()

# Wait for login to complete
time.sleep(5)

# Navigate to profile page
driver.get("https://www.naukri.com/mnjuser/profile")
time.sleep(5)

# Update the profile image
driver.find_element(By.XPATH, "//div[@class='photoBadge Pending']").click()
time.sleep(3)

# Upload image
upload_image = driver.find_element(By.ID, "fileUpload")
image_path = r'D:\certificate\pass.jpeg'  # Ensure the file path is correct and accessible
upload_image.send_keys(image_path)
time.sleep(5)

# Optional: Confirm the upload if there's any confirmation button to click
# Example:
# driver.find_element(By.XPATH, "//button[text()='Save']").click()

print("Profile image updated successfully!")

# Close the browser
driver.quit()
