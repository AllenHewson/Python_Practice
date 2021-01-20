# Save the url as a variable
import requests
from bs4 import BeautifulSoup
import lxml
url = 'https://scrapingclub.com/exercise/list_basic/'
# Create a one page scraper first
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
# Inspect the elements and grab the outer shell of each item
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
# Now that we have the outer shell of each item we can iterate through each and grab the text properties
# Name is in h4 with class card title, price is in h5
count = 1
for i in items:
    # When running the code initially it looks like a new line character occurs with the item name.
    # We patch that with the strip command
    itemName = i.find('h4', class_='card-title').text.strip('\n')
    itemPrice = i.find('h5').text
    print(f"{count} Price: {itemPrice}, \n Item Name: {itemName}")
    count += 1
