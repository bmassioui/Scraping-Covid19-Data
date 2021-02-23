# expose scraped data for covid19
from flask import Flask
import scraper
import helpers
import constants
import repository

app = Flask(__name__)

# returns all scraped data as JSON result
@app.route('/get', methods=["GET"])
def get():
    try:
        if(not helpers.is_datasource_exists()):
            return {'status code' : 412, 'Message' : 'Datasource unavailable, please refresh datasource!'}

        return repository.getall()
    except:
        return {'status code' : 500, 'Message' : 'Internal Server Error, please contact administrator.'}

# returns single record of WORLD's
@app.route('/get_4_world', methods=["GET"])
def get_4_world():
    try:
        if(not helpers.is_datasource_exists()):
            return {'status code' : 412, 'Message' : 'Datasource unavailable, please refresh datasource!'}

        return repository.get_4_world()
    except:
        return {'status code' : 500, 'Message' : 'Internal Server Error, please contact administrator.'}

# returns country's records
@app.route('/get_4_country', methods=["GET"])
def get_4_country(country):
   try:
        if(not helpers.is_datasource_exists()):
            return {'status code' : 412, 'Message' : 'Datasource unavailable, please refresh datasource!'}

        if()
            return {'status code' : 404, 'Message' : 'No data has been found!'}


        return repository.get_4_world()
    except:
        return {'status code' : 500, 'Message' : 'Internal Server Error, please contact administrator.'}

# refresh DATASOURCE(excel file .csv)
@app.route('/refresh', methods=["GET"])
def refresh():
    try:
        scraper.process()
        return {'status code' : 200, 'Message' : 'Datasource has been refreshed successfully!'}
    except:
        return {'status code' : 500, 'Message' : 'Unable to scrape covid19 data.'}


    
