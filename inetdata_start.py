# 
# Example file for retrieving data from the internet
#
import urllib.request


def main():
  webURL = urllib.request.urlopen('http://www.google.com')
  print(f"Result code: {webURL.getcode()}")
  # 200 means you can connect to the website with no errors, 404 means file not found
  data = webURL.read()
  print(data) # Should be the html code for Google's Homepage



if __name__ == "__main__":
  main()
