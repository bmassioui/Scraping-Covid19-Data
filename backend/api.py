# expose scraped data for covid19
from flask import Flask
from flask import request
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
            return {'status code': 412, 'Message': 'Datasource unavailable, please refresh datasource!'}

        return repository.getall()
    except Exception as exception:
        return {'status code': 500, 'Message':  exception.__doc__}

# returns single record of WORLD's


@app.route('/get_4_world', methods=["GET"])
def get_4_world():
    try:
        if(not helpers.is_datasource_exists()):
            return {'status code': 412, 'Message': 'Datasource unavailable, please refresh datasource!'}

        return repository.get_4_world()
    except Exception as exception:
        return {'status code': 500, 'Message':  exception.__doc__}

# returns country's records


@app.route('/get_4_country', methods=["GET"])
def get_4_country():
    country = request.args.get('country')
    try:
        if(not country):
            return {'status code': 404, 'Message': 'No data has been found!'}

        if(not helpers.is_datasource_exists()):
            return {'status code': 412, 'Message': 'Datasource unavailable, please refresh datasource!'}

        return repository.get_4_country(country)
    except Exception as exception:
        return {'status code': 500, 'Message':  exception.__doc__}

# refresh DATASOURCE(excel file .csv)


@app.route('/refresh', methods=["GET"])
def refresh():
    try:
        scraper.process()
        return {'status code': 200, 'Message': 'Datasource has been refreshed successfully!'}
    except Exception as exception:
        return {'status code': 500, 'Message': exception.__doc__}
