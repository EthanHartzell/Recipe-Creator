from urllib.request import urlopen
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import nltk


def scrapeIngredients(Food):
    cookie_page = "https://www.allrecipes.com/search/results/?wt=" + Food + "&sort=re"
    cookies = urlopen(cookie_page)
    cookieSoup = BeautifulSoup(cookies,'html.parser')
    for link in cookieSoup.find_all(class_ ="fixed-recipe-card__h3"):
        print("#####RECIPIE##########################")
        page = urlopen((link.a.get('href')))
        soup = BeautifulSoup(page, 'html.parser')
        name_box = soup.find_all(itemprop = 'ingredients')
        n = 1
        vars()['Recipie' + str(n)]= pd.DataFrame(columns = ['Quantity','Measurment','Adj','Adj2','Noun1','Noun2','Ingredient'],index=[np.arange(len(name_box))])
        n = n+1
        for i in range(0,len(name_box)): 
            x = (nltk.pos_tag(nltk.word_tokenize(''.join(name_box[i].contents))))
            for j in range(0,len(x)):
                if (x[j][1] == 'CD') & (pd.isnull(vars()['Recipie' + str(n-1)]['Quantity'][i]).all()):
                    vars()['Recipie' + str(n-1)]['Quantity'][i] = x[j][0]
                elif (x[j][1] == 'NN' or x[j][1] =='NNS' or x[j][1] == 'JJ') \
                    & (pd.isnull(vars()['Recipie' + str(n-1)]['Measurment'][i]).all()):
                    vars()['Recipie' + str(n-1)]['Measurment'][i] = x[j][0]
                elif (x[j][1] == 'JJ') \
                    & (pd.notnull(vars()['Recipie' + str(n-1)]['Measurment'][i]).all()) \
                    & (pd.isnull(vars()['Recipie' + str(n-1)]['Adj'][i]).any()):
                   vars()['Recipie' + str(n-1)]['Adj'][i] = x[j][0]
                elif (x[j][1] == 'JJ') \
                    & (pd.notnull(vars()['Recipie' + str(n-1)]['Measurment'][i]).all()) \
                    & (pd.notnull(vars()['Recipie' + str(n-1)]['Adj'][i]).any()) \
                    & (pd.isnull(vars()['Recipie' + str(n-1)]['Adj2'][i]).any()):
                   vars()['Recipie' + str(n-1)]['Adj2'][i] = x[j][0]
                elif (x[j][1] == 'NN' or x[j][1] =='NNS') \
                    & (pd.notnull(vars()['Recipie' + str(n-1)]['Measurment'][i]).all()) \
                    & (pd.isnull(vars()['Recipie' + str(n-1)]['Noun1'][i]).any()):
                   vars()['Recipie' + str(n-1)]['Noun1'][i] = x[j][0]
                elif (x[j][1] == 'NN' or x[j][1] =='NNS') \
                    & (pd.notnull(vars()['Recipie' + str(n-1)]['Measurment'][i]).all()) \
                    & (pd.notnull(vars()['Recipie' + str(n-1)]['Noun1'][i]).any()) \
                    & (pd.isnull(vars()['Recipie' + str(n-1)]['Noun2'][i]).any()):
                   vars()['Recipie' + str(n-1)]['Noun2'][i] = x[j][0]
                if (pd.isnull(vars()['Recipie' + str(n-1)]['Adj'][i]).any()) \
                    & (pd.isnull(vars()['Recipie' + str(n-1)]['Adj2'][i]).any()) \
                    & (pd.isnull(vars()['Recipie' + str(n-1)]['Noun1'][i]).any()) \
                    & (pd.isnull(vars()['Recipie' + str(n-1)]['Noun2'][i]).any()):
                    vars()['Recipie' + str(n-1)]['Ingredient'][i] = \
                    vars()['Recipie' + str(n-1)]['Measurment'][i]
                elif pd.isnull(vars()['Recipie' + str(n-1)]['Adj2'][i]).any():
                    if pd.isnull(vars()['Recipie' + str(n-1)]['Adj'][i]).any():
                        adj = ''
                    else: adj = vars()['Recipie' + str(n-1)]['Adj'][i]
                    if pd.isnull(vars()['Recipie' + str(n-1)]['Noun1'][i]).any():
                        N1 = ''
                    else: N1 = vars()['Recipie' + str(n-1)]['Noun1'][i]
                    if pd.isnull(vars()['Recipie' + str(n-1)]['Noun2'][i]).any():
                        N2 = ''
                    else: N2 = vars()['Recipie' + str(n-1)]['Noun2'][i]
                    vars()['Recipie' + str(n-1)]['Ingredient'][i] = \
                    adj + N1 + N2
                elif pd.notnull(vars()['Recipie' + str(n-1)]['Adj2'][i]).any():
                    if pd.isnull(vars()['Recipie' + str(n-1)]['Adj2'][i]).any():
                        adj = ''
                    else: adj = vars()['Recipie' + str(n-1)]['Adj2'][i]
                    if pd.isnull(vars()['Recipie' + str(n-1)]['Noun1'][i]).any():
                        N1 = ''
                    else: N1 = vars()['Recipie' + str(n-1)]['Noun1'][i]
                    if pd.isnull(vars()['Recipie' + str(n-1)]['Noun2'][i]).any():
                        N2 = ''
                    else: N2 = vars()['Recipie' + str(n-1)]['Noun2'][i]
                    vars()['Recipie' + str(n-1)]['Ingredient'][i] = \
                    adj + N1 + N2
        print(vars()['Recipie' + str(n-1)][['Quantity','Measurment','Ingredient']])





scrapeIngredients("chocolatechipcookies")



