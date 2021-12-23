import requests
import json
from bs4 import BeautifulSoup

# test_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'html.parser')
# print(test_soup.prettify())

# l = test_soup.find_all('b')

# print(test_soup('b').parent)



to_visit = set()
response = requests.get('http://home.ku.edu.tr/~sunver/')

soup=BeautifulSoup(response.content,'html.parser')

# print(soup.prettify())
print(soup.find_all('a'))


# print(soup.head.contents[0])
#
# head_tag = soup.head.contents[0]

# for child in head_tag.children:
#     print(child)
#
# Unver = soup.find_all(text='Ünver')
#
# print(Unver[2].parent)


# for a in soup.select('Ünver'):
#     to_visit.add(a.get('Ünver'))
#
# print(to_visit)

