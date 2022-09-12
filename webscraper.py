from bs4 import BeautifulSoup
import pandas as pd
from lxml import etree
import requests
import csv
import numpy as np


url = "https://www.imdb.com/chart/top/"
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'lxml')

dom = etree.HTML(str(soup))
table = soup.find('table', class_='chart full-width')
movies = soup.find('td', class_ = 'titleColumn')


table in soup.find_all('table')
table = soup.find('table', class_='chart full-width')

#defining the data frame
df = pd.DataFrame(columns=['cNum', 'Title', 'Ratings'])

#collecting Ddata
for row in table.tbody.find_all('tr'):
    #finding all data for each column
    columns = row.find_all('td') #gets all columns
    extra = row.find_all('a') #title
    if(columns != []):
        titleCol = columns[1].text.strip()
        titleColA = extra[1].text.strip()
        ratingsCol = columns[2].text.strip()
        df_new_row = pd.DataFrame({'cNum': titleCol, 'Title': titleColA, 'Ratings': ratingsCol}, index = [0])
        df = pd.concat([df, df_new_row], ignore_index= True)

#print(df)
df.to_csv('movies.csv')
print("completed")
