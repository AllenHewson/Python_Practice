import requests
from bs4 import BeautifulSoup
import lxml
# Web scraping involves getting the html source code from websites and then parsing it as a way to scrape a website for
# certain types of data


# First save the url as a variable
url = "https://quotes.toscrape.com/"
# Use get function from requests to ping the web address and get the html source code from the website.
response = requests.get(url)
# Now parse the html document using beautifulsoup and lxml
soup = BeautifulSoup(response.text, 'lxml')
# All the quotes have the span tag and the class text.
# Use this information and the find_all function to extract all of the quotes.
quotes = soup.find_all('span', class_='text')
# quotes now has all the quotes on the site as well as some html in it.
# Now we will use the find all function to grab the authors names for each quote
authors = soup.find_all('small', class_='author')
# Now we will grab the tags for each quote
# Because there are multiple tags for each quote we will focus on exracting the div tags, which divide quotes.
tags = soup.find_all('div', class_='tags')
# Now use the find all function again in the tags variable to find the tags for each quote
# This is done in the for loop
# This for loop removes the excess html and prints each quote and then the author
for i in range(0, len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)

