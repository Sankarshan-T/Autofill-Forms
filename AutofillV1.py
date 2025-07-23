from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://docs.google.com/forms/d/e/1FAIpQLScjTv8IAPT4G6qqQ5_3cxqIw8xioVv9W7MJTBZ03uY8Im1CFA/viewform?usp=dialog")

wait = WebDriverWait(driver, 10)

# Fill "Name"
wait.until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="text"])[1]'))).send_keys("Steve")

#Fill age:
age_input = wait.until(EC.element_to_be_clickable((By.XPATH, '(//input[@type="text"])[2]')))
age_input.send_keys("25")

# Click Submit
wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Submit"]/ancestor::div[@role="button"]'))).click()

driver.quit()