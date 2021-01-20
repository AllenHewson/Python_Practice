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

# Now that we have a single page web scraper set up, we will make it one that scrapes multiple pages
# Inspecting the page selector at the bottom of the web page shows that the links are stored in href tags
# Create a list to hold the links of each page
# To do this we will narrow our search to the pagination class.
pages = soup.find('ul', class_='pagination')
# Extract the links
urls = []
links = pages.find_all('a', class_='page-link')
# We will also convert the links we extract to integers, and pass if this is not possible.
# This way we avoid making duplicate data through the next and previous page buttons when web scraping.
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    # Now add the links that are numbers
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
# Now loop through each url in the list, add it to the base url, create a new request and scrape the page
for i in urls:
    newurl = url + i
    response = requests.get(newurl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        # When running the code initially it looks like a new line character occurs with the item name.
        # We patch that with the strip command
        itemName = i.find('h4', class_='card-title').text.strip('\n')
        itemPrice = i.find('h5').text
        print(f"{count} Price: {itemPrice}, \n Item Name: {itemName}")
        count += 1
