from bs4 import BeautifulSoup
import urllib.request

TABLE_OF_CONTENTS = "https://parahumans.wordpress.com/table-of-contents/"

fp = urllib.request.urlopen(TABLE_OF_CONTENTS)
my_bytes = fp.read()

my_str = my_bytes.decode("utf8")
fp.close()

urls = []

soup = BeautifulSoup(my_str, 'html.parser')
my_links = soup.find("div", class_='entry-content')
for link in my_links.find_all('a', href=True):
    substring_one = 'twitter'
    substring_two = 'facebook'
    if substring_two not in link['href'] and substring_one not in link['href']:
        urls.append(link['href'])

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