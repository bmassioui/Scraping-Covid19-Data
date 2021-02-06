# centralize scraping business logic
import requests
from bs4 import BeautifulSoup
import pandas as pd
import dask.dataframe as dd
import constants

def process():
    page = requests.get(constants.SCRAPED_FROM)
    if(page.status_code != 200):
        raise Exception('unable to process scraping')

    # parsing the result to xml format    
    soup = BeautifulSoup(page.content, 'lxml')
    table = soup.find(constants.TAG_2_SCRAPE, attrs={'id': constants.TAG_ID_2_SCRAP}) 
    # extract only the rows withing the table that have style property is null as value (Rows that conatins data is only those that have style is null)
    rows = table.find_all("tr", attrs={"style": ""})
    data = []
    for item in rows:
        data.append(item.text.strip().split("\n")[:12])
    
    dt = pd.DataFrame(data)
    df = dd.from_pandas(dt,npartitions=1)
    df.head()

    # save scraped data to .csv as datasource
    df.to_csv(constants.PATH_WHERE_2_SAVE_DATASOURCE)