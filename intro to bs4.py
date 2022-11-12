import bs4 as bs 
import urllib.request  

source  = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(source,'lxml')

print(soup.title.string) #this will print the title

print(soup.find_all('p'))


# for paragraph in soup.find_all('p'): #this will print all paragraph text
#     print(paragraph.text)

# to get all the text from the page you could do

#print(soup.get_text())

#to get all the urls you could do
for url in soup.find_all('a'):
    print(url.get('href'))





