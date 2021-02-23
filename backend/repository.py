import pandas as pd
import constants
"""
Datasource repository (Design pattern)
"""

# get datasource as dataframe
def get():
    datasource_path =  constants.DATASOURCE_PATH.replace("*", "0")
    df = pd.read_csv(datasource_path)
    return df.head()

# ret all records as Json Response
def getall():
    result = get()
    return result.to_json(orient="records")

# get record for "world" as Json Response
def get_4_world():
    df = get()
    result = df[df["Country,Other"] == "World"]
    return result.to_json(orient="records")

# get country record as Json Response
def get_4_country(country):
    df = get()
    result = df[df["Country,Other"] == country]
    return result.to_json(orient="records")
