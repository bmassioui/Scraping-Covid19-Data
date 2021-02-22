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
    print('start')
    df = get()
    print(df)
    # df.loc[df[""Country,Other"] == "World"]
    print(df[df["7"] == "ActiveCases"])
    print('end')
    # return df.head()
