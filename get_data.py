import pandas as pd
from datetime import datetime
import os

import yaml
import logging

from data_names import get_data_by_name


# create the data and logs directories if they don't exist
if not os.path.exists('data'):
    os.makedirs('data')
if not os.path.exists('logs'):
    os.makedirs('logs')

# configure the logger to write to a log file and to the console
logging.basicConfig(filename='logs/output.log', level=logging.DEBUG,format='%(asctime)s %(levelname)s: %(message)s')
logger = logging.getLogger()
logger.addHandler(logging.StreamHandler())

# load the configuration file
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)


def main():
    # log the start of the data retrieval process
    logger.info('Get data.')
    # iterate through each data type specified in the configuration file
    for data_name in config['data_names']:
        # determine the name of the data type and its abbreviation
        dtype, dtype_name = get_data_by_name(data_name)
        dataset = get_ons_data_frames(dtype, dtype_name)
        # date_name = str(config['first_year']) +'_'+ str(config['last_year'])
        dataset.to_csv('data/'+f'{dtype_name}.csv', sep=';', index=False)


def get_ons_data_frames(dtype, dtype_name):
    # create an empty list to hold the data frames for each year
    df_list = []
    current_year = datetime.now().year
    # iterate through each year from the first year specified in the configuration file to the current year
    for year in range(config['first_year'], config['last_year']+1):
        url = f'https://ons-dl-prod-opendata.s3.amazonaws.com/dataset/{dtype}{year}.csv'
        try:
            # attempt to read the data from the URL into a data frame
            df = pd.read_csv(url, sep=';').round(3)
            # log the successful retrieval of the data for the given data type and year
            logger.info(f"Getting {dtype_name} data from the year {year}.")
            # add the data frame to the list of data frames for the given data type
            df_list.append(df)
        except:
            # log a warning if the data for the given data type and year is not available
            logger.warning(f"Data {dtype_name} not available for the year {year}.")
            continue
    df_all = pd.concat(df_list)
    logger.info(f'Download {dtype_name} data complete!')
    return df_all
    
    

if __name__ == '__main__':
    main()