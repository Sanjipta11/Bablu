from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.naukri.com/nlogin/login")
driver.maximize_window()

driver.find_element(By.ID,"login_Layer").click()
driver.implicitly_wait(4)
driver.find_element(By.ID,"usernameField").send_keys("sanjipt330@gmail.com")
driver.find_element(By.ID,"passwordField").send_keys("Sanjipt@2024")
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"#loginForm > div:nth-child(2) > div.action.row.mb0 > div > button.waves-effect.waves-light.btn-large.btn-block.btn-bold.blue-btn.textTransform").click()
driver.find_element(By.XPATH,"/html/body/main/div/div/div[3]/div/div[3]/div[2]/a").click()
time.sleep(3)
naukri_logo = driver.find_element(By.XPATH,"(//a[@class='nI-gNb-header__logo nI-gNb-company-logo'])").click()
time.sleep(5)
view_profile = driver.find_element(By.XPATH,"//div[@class='view-profile-wrapper']")
view_profile.click()
driver.implicitly_wait(3)
# upload resume
# upload_resume = driver.find_element(By.XPATH,"//input[@class='dummyUpload typ-14Bold']")
# time.sleep(4)
# file_path = r'C:\Users\sanji\Desktop\sanjipt_Auto_tester3.5.pdf'
# upload_resume.send_keys(file_path)
# time.sleep(5)

# update the profile image
# driver.find_element(By.XPATH,"//div[@class='photoBadge Pending']").click()
# time.sleep(5)
# upload_image = driver.find_element(By.ID,"fileUpload")
# image_path = r"D:\certificate\pass.jpeg"
# upload_image.send_keys(image_path)
# driver.find_element(By.ID,"submit").click()
# time.sleep(5)

# Edit profile details designation

driver.find_element(By.XPATH,"//em[@class='icon edit']").click()
time.sleep(5)
driver.find_element(By.ID,"name").send_keys("sanjipta kumar raut")
driver.find_element(By.XPATH,"//input[@id='exp-years-droopeFor']").send_keys("4 years")



