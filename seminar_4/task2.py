import requests
from lxml import html
import pandas as pd
url = "https://www.worldathletics.org/records/toplists/sprints/60-metres/indoor/women/senior/2023?page=1"

response = requests.get(url, headers={
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'})

tree = html.fromstring(response.content)

table_rows = tree.xpath("//table[@class='records-table']/tbody/tr")

list_date = []
for row in table_rows:
    columns = row.xpath(".//td/text()")
    list_date.append({
        'rank' : columns[0].strip(),
        'mark' : columns[1].strip(),
        'wind' : columns[2].strip(),
        'Competitor' : row.xpath(".//td[4]/a/text()")[0].strip(),
        'DOB' : columns[5].strip(),
        'Nat' : columns[7].strip(),
        'Pos' : columns[8].strip(),
        'venue' : columns[9].strip(),
        'date' : columns[10].strip(),
        'result_score' : columns[11].strip(),
    })
print(list_date)

df = pd.DataFrame(list_date)
print(df.head())