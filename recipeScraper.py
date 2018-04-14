from urllib.request import urlopen
from bs4 import BeautifulSoup
quote_page = "https://www.allrecipes.com/recipe/15300/tinas-shortbread-chocolate-chip-cookies/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202"
page = urlopen(quote_page)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find_all(itemprop = 'ingredients');

for i in range(0,len(name_box)):
    print(name_box[i].contents)


