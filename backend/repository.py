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

# get record for ""world
def get_4_world():
    df = get()
    df[df["Country,Other"] == "World"]
    return df.head()
