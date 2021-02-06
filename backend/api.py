# expose scraped data for covid19
from flask import Flask
import scraper
import helpers

app = Flask(__name__)

# returns all scraped data as JSON result
#@app.route('/get')
#def get():
#    return {}

# returns single record of WORLD's
@app.route('/get_4_world', methods=["GET"])
def get_4_world():
    if(not helpers.is_datasource_exists()):
        return {'status code' : 412, 'Message' : 'Datasource unavailable, please refresh datasource!'}

    return {'time' : 'test'}

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