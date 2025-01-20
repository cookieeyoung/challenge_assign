import requests
import pandas as pd

url = "http://ecos.bok.or.kr/api/StatisticSearch/ULZSIIHE0GZR6O0QLP2O/json/kr/1/100/801Y002/A/2020/2024/1090000/"
response = requests.get(url)

data = response.json()
df = data['StatisticSearch']["row"]
df2 = pd.DataFrame(df)

df2 = df2[['STAT_CODE','STAT_NAME','ITEM_CODE1','UNIT_NAME','WGT','TIME','DATA_VALUE']]
df2.head(10)
