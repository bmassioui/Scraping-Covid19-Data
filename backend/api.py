# expose scraped data for covid19
from flask import Flask
import scraper
import helpers
import constants
import repository

app = Flask(__name__)

# returns all scraped data as JSON result
#@app.route('/get')
#def get():
#    return {}

# returns single record of WORLD's
# @app.route('/get_4_world', methods=["GET"])
# def get_4_world():
#     try:
#         if(not helpers.is_datasource_exists()):
#             return {'status code' : 412, 'Message' : 'Datasource unavailable, please refresh datasource!'}

#         df = repository.get_4_world()
        
#         return {'status code' : 200, 'Message' : 'Datasource has been refreshed successfully!'}
#     except:
#         return {'status code' : 500, 'Message' : 'Internal Server Error, please contact administrator.'}

# returns country's records
#@app.route('/get_4_country')
#def get_4_country():
#    return {}

# refresh DATASOURCE(excel file .csv)
@app.route('/refresh',  methods=["GET"])
def refresh():
    try:
        scraper.process()
        return {'status code' : 200, 'Message' : 'Datasource has been refreshed successfully!'}
    except:
        return {'status code' : 500, 'Message' : 'Unable to scrape covid19 data.'}


    
