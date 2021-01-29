# Many websites use asynchronous techniques to load content more quickly and dynamically
# This causes issues with Selenium trying to locate an element that isn't yet loaded.
# Wait functions add crucial time intervals in between actions performed
# This allows elements to load before they are interacted with.
# Explicit Wait Functions: Wait until a condition is satisfied before executing
# Implicit Wait Functions: Wait for a certain amount of time until the element becomes avaliable

# To practice with wait functions we will use Google Earth which uses ajax to asynchronously load its content
# When initially loading the webpage, the top banner appears a little after everything else
# If we wanted to click the "Launch Earth in Chrome" Button we will have to use an explicit wait function
from selenium import webdriver
# A few new extensions will also need to be added to use explicit wait functions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
# Load the url into the driver
driver.get('https://www.google.com/earth/')
# Now create the wait, an explicit wait can be created using the WebDriverWait function
# This function will create an exception after 10 seconds if the condition we make is not satisfied
wait = WebDriverWait(driver, 10)
# Now a condition must be created for the explicit wait. This is done with the expected_conditions module
# The condition will be to wait, until the launch Earth in Chrome button becomes clickable.
# Grab the xpath of the button
launchEarthButton = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/header/div/nav[1]/ul[2]/li[2]/a/span/span')))
launchEarthButton.click()
