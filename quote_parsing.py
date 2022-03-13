import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_='text')
author = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
dict_quotes_author = {}
list_quotes_info = []
# for q in quotes:
#     dict_quotes_author[q.text] = author[quotes.index(q)].text
# print(dict_quotes_author)
for i in range(len(quotes)):
    tags_list = []
    for tag in tags[i].find_all('a', class_='tag'):
        tags_list.append(tag.text)
    dict_quotes_info = {'id': i+1, 'quotes': quotes[i].text, 'author': author[i].text, 'tags': tags_list}
    list_quotes_info.append(dict_quotes_info)
print(list_quotes_info)