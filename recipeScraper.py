from urllib.request import urlopen
from bs4 import BeautifulSoup
quote_page = "https://www.allrecipes.com/recipe/15300/tinas-shortbread-chocolate-chip-cookies/?internalSource=hub%20recipe&referringContentType=search%20results&clickId=cardslot%202"
page = urlopen(quote_page)
soup = BeautifulSoup(html_doc, "html.parser")
name_box = soup.find_all("span", attrs={"itemprop": "ingredients"})
name = name_box.text.strip() 
print(name)
name_box = soup.find_all("span", attrs={"itemprop": "ingredients"})
   

print(name_box)

