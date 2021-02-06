# expose scraped data for covid19
from flask import Flask
import scraper

app = Flask(__name__)

# returns all scraped data as JSON result
#@app.route('/get')
#def get():
#    return {}

# returns single record of WORLD's
#@app.route('/get_4_world')
#def get_4_world():
#     return {}

# returns country's records
#@app.route('/get_4_country')
#def get_4_country():
#    return {}

# refresh DATASOURCE(excel file .csv) by re-scraping 
@app.route('/refresh',  methods=["GET"])
def refresh():
    try:
        scraper.process()
        return {'status code' : 200, 'Message' : 'Datasource has been refreshed successfully!'}
    except:
        return {'status code' : 500, 'Message' : 'Unable to scrape covid19 data.'}