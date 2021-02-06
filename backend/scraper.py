# centralize scraping business logic
import requests
from bs4 import BeautifulSoup
import pandas as pd
import dask.dataframe as dd
import constants

"""
 Process COVID 19 web scraping
"""
def process():
    page = requests.get(constants.SCRAPED_FROM)
    if(page.status_code != 200):
        raise Exception('unable to process web scraping')

    # parsing the result to xml format    
    soup = BeautifulSoup(page.content, 'lxml')
    table = soup.find(constants.TAG_2_SCRAPE, attrs={'id': constants.TAG_ID_2_SCRAP}) 
    # extract only the rows withing the table that have style property is null as value (Rows that conatins data is only those that have style is null)
    rows = table.find_all("tr", attrs={"style": ""})

    data = []
    for i,item in enumerate(rows):
        if i == 1:
            data.append(item.text.strip().split("\n")[:12])
        else:
            data.append(item.text.strip().split("\n")[1:12])

    dt = pd.DataFrame(data)
    df = dd.from_pandas(dt,npartitions=1)

    df.head()

    # save scraped data to .csv as DATASOURCE
    df.to_csv(constants.DATASOURCE_PATH)