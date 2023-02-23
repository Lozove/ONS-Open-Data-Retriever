import pandas as pd
import yaml

# load the configuration file
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

for data in config['all_data']:
    df = pd.read_csv('data/' + data + '.csv', sep=';')
    print(f'Arquivo relativo aos dados de {data}')
    print(df)