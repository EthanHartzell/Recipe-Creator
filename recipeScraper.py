from urllib.request import urlopen
from bs4 import BeautifulSoup


def scrapeIngredients(Food):
    cookie_page = "https://www.allrecipes.com/search/results/?wt=" + Food + "&sort=re"
    cookies = urlopen(cookie_page)
    cookieSoup = BeautifulSoup(cookies,'html.parser')
    for link in cookieSoup.find_all(class_ ="fixed-recipe-card__h3"):
        print("#####RECIPIE##########################")
        page = urlopen((link.a.get('href')))
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find_all(itemprop = 'ingredients')
        for i in range(0,len(name_box)):
            print(name_box[i].contents)



scrapeIngredients("chocolatechipcookies")

scrapeIngredients("chocolatechipcookies")
