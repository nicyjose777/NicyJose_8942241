import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the Chrome webdriver
driver = webdriver.Chrome()

# Open the Flipkart website
driver.get("https://www.flipkart.com/")

# Wait for the page to load
time.sleep(2)

home_page_url = driver.current_url

#Click on the fashion element
driver.find_element(By.XPATH, "//span[text()='Fashion']").click()
time.sleep(2)

#Display women ethnics
women_ethnic=driver.find_element("xpath","/html/body/div[4]/div[1]/object/a[3]")
#Click on women ethnic
women_ethnic.click()
time.sleep(2)

#Display Flight page
flights = driver.find_element("xpath", "/html/body/div/div/div[2]/div/div/a[1]")
#Click on the flights
flights.click()
time.sleep(10)

#Home page is reloaded
driver.get("https://www.flipkart.com/")
time.sleep(8)

#Display grocery page
grocery = driver.find_element("xpath", "/html/body//div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/a[1]/div/div/div/div/img")
grocery.click()
time.sleep(10)

driver.get("https://www.flipkart.com/")
#Display Mobiles
mobiles=driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/a[2]/div/div/span/span")
mobiles.click()
time.sleep(10)

# Close the browser
driver.quit()
