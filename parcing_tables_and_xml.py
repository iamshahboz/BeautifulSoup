import bs4 as bs  
import urllib.request

# source = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

# soup = bs.BeautifulSoup(source,'lxml')

# table = soup.table  
# # print(table)

# table_rows = table.find_all('tr')

# for tr in table_rows:
#     td = tr.find_all('td')
#     row= [i.text for i in td]
#     print(row)


#this is for xml
source = urllib.request.urlopen('https://pythonprogramming.net/sitemap.xml').read()

soup = bs.BeautifulSoup(source,'xml')
print(soup)