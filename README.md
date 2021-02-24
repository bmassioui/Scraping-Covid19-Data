# Scraping-Covid19-Data (BEGINNER LEVEL)
With various attempt to clamp down the effect of COVID19 on the world, various research works and innovative measures depends on insights gained from the right data. Most of the data required to aid innovations may not be available via Application Programming Interface (API) or file formats like ‘.csv’ waiting to be downloaded, but can only be accessed as part of a web page. All code snippet can be found here.
Web scraping is a term used to describe the use of a program or algorithm to extract and process large amounts of data from the web. Whether you are a data scientist, engineer, or anybody who analyzes large amounts of datasets, the ability to scrape data from the web is a useful skill to have.
Worldometers has a credible sources of COVID19 data around the world. In this article, we will learn how to scrape COVID19 data depicted below from a web page to a Dask dataframe from the site using python.

# Techs
1. Python
2. Flask
3. Pandas
4. Dask
5. Beautifulsoup4

# Where can i find the scraped data ?
> backend/data/datasource-*.csv

# About the project
The project is a Flask Api, which exposes 4 differents endpoints :
1. Refresh datasource (scraping the covid 19 statistic and export it as .csv file)
2. Get statistic for the world (new cases, recovered, total death ...)
3. Get statistic by specific country (new cases, recovered, total death ...)
4. Get statistic for all available countries (new cases, recovered, total death ...)

# How to run the project
First of all, the project use local environement, therfore to run the project successfully, it requires to install its dependencies:
1. Clone the repository 
2. Withing the backend directory, run the following command (via terminal/cmd ..)
    `$ python3 -m venv venv`
3. Then
    `venv\Scripts\activate`
4. Then
    `pip install flask python-dotenv`
5. Finally,
    `flask run`
6. Navigate to :
    `127.0.0.1:5000`


# How to invoke each endpoints
1. Run the scrap `127.0.0.1:5000/refresh`
2. For **WORLD** `127.0.0.1:5000/get_4_world`
3. For **COUNTRY** `127.0.0.1:5000/get_4_country?country=country_name`, Note `country_name` is the country that need to be passed.
4. For **ALL** `127.0.0.1:5000/get`

The result is a JSON response for the all endpoints



## References
1. [Covid 19 web scraping](https://towardsdatascience.com/scraping-covid19-data-using-python-80120eb5eb66) 
2. [Flask basics setup](https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project)
