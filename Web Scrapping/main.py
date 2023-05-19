import requests
from bs4 import BeautifulSoup

url = "https://www.codewithharry.com/"

# step1: get the html
r = requests.get(url)
htmlContent = r.content

# step2: Parse the 
soup = BeautifulSoup(htmlContent,'html.parser')

# step3: html tree traversal 
# get all the links
all_links = set()
anchors = soup.find_all('a')
for link in anchors:
    if(link != '#'):
        l = url+link.get('href')
        all_links.add(l)
        print(l)





# Extras
# title = soup.title
# print(title)
# print(type(title))
# print(title.string)
# paras = soup.find_all('p')
# print(paras)
# ancors = soup.find_all('a')
# print(ancors)
# print(soup.find('p'))
# print(soup.find('p'))
# print(soup.find('p')['class'])
# find all the elements with class lead 
# print(soup.find_all("p", class_="mt-2"))
# print(soup.find('p').get_text())


