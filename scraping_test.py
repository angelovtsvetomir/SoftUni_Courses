# This is a simple project which scrapes information for different chapters from a website.
# The steps I have taken are described in the comments.

# Importing required libraries.

from bs4 import BeautifulSoup
import urllib.request

# Opening, reading and closing the initial page, where we will get our data from.

TABLE_OF_CONTENTS = "https://parahumans.wordpress.com/table-of-contents/"
fp = urllib.request.urlopen(TABLE_OF_CONTENTS)
my_bytes = fp.read()
my_str = my_bytes.decode("utf8")
fp.close()

# Creating an empty list where we will store every chapter's URL.
# Creating the soup and passing a string from the webpage through it, then finding the specific
# part of the webpage we need.

urls = []
soup = BeautifulSoup(my_str, 'html.parser')
my_links = soup.find("div", class_='entry-content')

# Looping through all the matching URL's and appending only the ones that lead to a chapter.
# I have excluded some of them which had the purpose of sharing content on social media.

for link in my_links.find_all('a', href=True):
    substring_one = 'twitter'
    substring_two = 'facebook'
    if substring_two not in link['href'] and substring_one not in link['href']:
        urls.append(link['href'])

# Creating a txt file, a new soup and looping through every URL that was saved in the list, then
# extracting the required text and saving it in the file. Finally, closing the txt file.

with open(f'ebook/ebook.txt', 'w', encoding="utf-8") as f:
    for element in urls:
        url_open = urllib.request.urlopen(element)
        my_bytes = url_open.read()
        my_string = my_bytes.decode("utf8")
        url_open.close()

        soup_two = BeautifulSoup(my_string, 'html.parser')
        chapter_content = soup_two.find("div", class_='entry-content')
        paragraphs = chapter_content.find_all('p')
        for paragraph in paragraphs:
            f.write(paragraph.getText() + "\n")
f.close()