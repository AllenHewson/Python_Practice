# Most things automated by selenium can be accomplished in a single line of code.
# This script will automate solving a drag and drop, something that takes 3 steps (picking up, dragging, and dropping)
# Will use the selenium library and chrome driver.
from selenium import webdriver
# To implement a drag and drop in selenium, action chains must be imported
from selenium.webdriver.common.action_chains import ActionChains
# Initialize the webdriver
driver = webdriver.Chrome()
# For viewing purposes maximize the window
driver.maximize_window()
# Get the url with the web driver
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
# Now we have to specify the source and destination elements
# This can be done with the inspect tool again and copying the xpath
# Click on the washington box in inspect and copy the xpath for the source
source = driver.find_element_by_xpath('//*[@id="box3"]')
# Then click on the United States box in inspect and copy the xpath for the destination
destination = driver.find_element_by_xpath('//*[@id="box103"]')
# Using the action chains library, more complex tasks like drag and dropping can be performed.
actions = ActionChains(driver)
# When methonds are called for actions on an actionschain, they are stored in a queue 
# Call the drag and drop function on the actions object