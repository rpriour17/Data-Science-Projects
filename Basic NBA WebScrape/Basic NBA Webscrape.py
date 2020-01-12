import requests
from bs4 import BeautifulSoup 
import pandas as pd

url = "https://www.basketball-reference.com/leaders/pts_per_g_season.html"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', attrs={'id':'stats_NBA'})
rows = table.find_all('tr')
columns = ['Rank', 'Player', 'PPG', 'Season']
table_Rows = []

for row in rows:
    cols = row.find_all('td')
    if cols:
        cols = [item.text.strip() for item in cols]
        table_Rows.append([item for item in cols]) #This Deletes an empty column

resultsDF = pd.DataFrame(table_Rows, columns=columns)

resultsDF.to_csv('NBA.csv')