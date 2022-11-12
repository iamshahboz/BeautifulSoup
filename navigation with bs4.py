import bs4 as bs  
import urllib.request

source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(source,'lxml')

# nav = soup.nav
# print(nav)

#this should give us all the links that it finds at the navbar
# for url in nav.find_all('a'):
#     print(url.get('href'))

#if you want to get all the div tag text you could do 
for div in soup.find_all('div'):
    print(div.text)