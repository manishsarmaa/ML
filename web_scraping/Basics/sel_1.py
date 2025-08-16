import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

url = 'https://google.com'
driver.get(url)
driver.maximize_window()
# # driver.add_credential('manishsarmaa','Manish@2')
time.sleep(1)


search_xpath = '//*[@id="APjFqb"]'
search = driver.find_element(by = By.XPATH, value = search_xpath)
search.send_keys('Data Engineering')
# search.send_keys('Selenium Python')
search.send_keys(Keys.ENTER)

time.sleep(3)

# #sign in 

# sign_in_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a/div'
# sign_in = driver.find_element(by = By.XPATH, value = sign_in_xpath)
# sign_in.click()
# time.sleep(8)

# phone_xpath = '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[1]'
# # phone_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'
# phone = driver.find_element(by = By.XPATH, value = phone_xpath)
# phone.send_keys('7863813859')
# time.sleep(1)

# phone.send_keys(Keys.ENTER)
# time.sleep(2)


# next_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div'
# next_button = driver.find_element(by = By.XPATH, value = next_xpath)
# next_button.click()
# time.sleep(7)

# print(f"Current URL: {driver.current_url}")
# print(f"Title : {driver.title}")
# driver.save_screenshot('x.png')

# time.sleep(5)

# driver.quit()