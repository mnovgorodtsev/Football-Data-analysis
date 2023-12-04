import requests
import pandas as pd
from bs4 import BeautifulSoup

page_link='https://www.ekstraklasa.org/statystyki/druzynowe'
r=requests.get(page_link)

soup=BeautifulSoup(r.text,'html.parser')

column_names=['Table pos','Team name','Points','Home Points', 'Away Points', 'Wins','Draws','Loses','Possesion %','Goals','Goals against',
              'Goal diff','Conversion rate','X goals','X goals per game','X goals against','X goals against per game',
              'Shots per game','Acc shots per game','Fouls','Fouled','Distance/game','Sprints/game','Yellow Cards','Red Cards']

float_columns=['Points','Home Points', 'Away Points', 'Wins','Draws','Loses','Possesion %','Goals','Goals against',
              'Goal diff','Conversion rate','X goals','X goals per game','X goals against','X goals against per game',
              'Shots per game','Acc shots per game','Fouls','Fouled','Distance/game','Sprints/game','Yellow Cards','Red Cards']

df = pd.DataFrame(columns=column_names)

web_table=soup.find('table', class_='_custom-table w-full _stuck')
raw_stats_table=[]

for single_stat_row in web_table.find_all('tr', class_='ng-star-inserted'):
    td_elements = single_stat_row.find_all('td')
    team_stat_row=[]
    for single_data in td_elements:
        team_stat_row.append(single_data.text)
    raw_stats_table.append(team_stat_row)

stats_dataframe = pd.DataFrame(raw_stats_table,columns=column_names)
stats_dataframe.set_index('Table pos', inplace=True)
stats_dataframe[float_columns]=stats_dataframe[float_columns].astype(float)

stats_dataframe.to_csv('ekstraklasa_table')
print(stats_dataframe)


