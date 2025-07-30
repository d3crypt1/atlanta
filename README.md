# Atlanta Residential Sales
![Atlanta Neighborhoods](app.png)

## Description
Atlanta Neighborhood Annual Mean Sale Prices from 2016-2024 displayed on a map with color indicating price.  Can hover over neighborhood in the map to see the mean and average sale price and number of sales.

## Tech basics
This repository can be used to build and run a docker container or simply run locally.

Developed in python.

### Local test run from terminal:
* Clone or download this repository eg:
`git clone https://github.com/d3crypt1/atlanta.git`
* From the atlanta_sales_app directory:
`streamlit run atlanta_sales_streamlit.py`

### To build/run usin docker-compose
* From terminal in the atlanta_sales_app directory:
`docker-compose up -d --build`

## Screenshot of hover
![Hover](app_hover.png)
