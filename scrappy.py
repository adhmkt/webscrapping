import requests
from bs4 import BeautifulSoup

# URL of the news website
url = 'https://cobusgreyling.medium.com/openai-announced-28-models-to-be-switched-off-6cb644735883'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the article title (hypothetical example - update based on HTML structure)
article_title = soup.find('h1')  # Replace 'h1' with the correct tag or class

# Extract and print the article title
if article_title:
#  print(article_title.text.strip())
    print(response.text);
else:
    print("Article title not found.")
