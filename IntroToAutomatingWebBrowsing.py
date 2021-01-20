# Automating web browsing can be used to test a website's functionality around the clock while saving resources
# It can make cross-browser proofing easier.
# Automating web browsing can also be used for botting processes. These are software that execute commands or routine
# tasks without the users intervention. Can script repetitive tasks such as filling out forms or logging in.
# It is also used to provide an advantage for limited quantity items such as tickets to shows and exclusive merchandise
from selenium import webdriver
# Initialize the webdriver
driver = webdriver.Chrome()
# First get the url with the driver
driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
# At this point, the code will open up a browser and then change the url to the one specified in the get function

# We will create a program that writes Hello World in the first input field and then clicks the show message button
# First we define what element we want to interact with, this can be done using the inspector tool.
# Inspect the element we want to interact with, and then right click on the highlighted html text and select copy xpath
# Use the find element by xpath function with the copied xpath to define the element we will interact with
messageField = driver.find_element_by_xpath('//*[@id="user-message"]')
# Now we can interact with this element, since this is an input box we pass an input to it through the send keys method
messageField.send_keys('Hello World')
# Now we need to click the show message button.
# Like before, use inspect to define the show message button
showMessageButton = driver.find_element_by_xpath('//*[@id="get-input"]/button')
# To click the button, we can just use selenium click method
showMessageButton.click()

# Now we will move onto the second part with the two input fields.
# Again use inspect to define the elements, then use send_keys to fill both of them out.
firstMessageField = driver.find_element_by_xpath('//*[@id="sum1"]')
secondMessageField = driver.find_element_by_xpath('//*[@id="sum2"]')
# Now fill out both of them with values
firstMessageField.send_keys('10')
secondMessageField.send_keys('11')
# Now grab the get total button
getTotalButton = driver.find_element_by_xpath('//*[@id="gettotal"]/button')
# Finally press the button
getTotalButton.click()
