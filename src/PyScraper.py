import requests
from bs4 import BeautifulSoup

# the URL to parse
base_url = 'http://www.nytimes.com'

# Open a handle to the specified page
r = requests.get(base_url)
# Create the soup, containing parsed markup
soup = BeautifulSoup(r.text)
# print a pretty version of the markup
print soup.prettify()
# find and loop through all elements on the page with the
# class name "story-heading"
for story_heading in soup.find_all(class_="story-heading"):
    # for the story headings that are links, print out the text
    # and format it nicely
    # for the others, take the contents out and format it nicely
    if story_heading.a:
        print(story_heading.a.text.replace("\n", " ").strip())
    else:
        print(story_heading.contents[0].strip())