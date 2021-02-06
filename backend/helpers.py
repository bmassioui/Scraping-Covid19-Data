import os.path
import constants as constants

"""
Verify the datasource's availibilty
"""
def is_datasource_exists():
    datasource_path =  constants.DATASOURCE_PATH.replace("*", "0")
    if (os.path.isfile(datasource_path) and os.access(datasource_path, os.R_OK)):
        return True
    
    return False