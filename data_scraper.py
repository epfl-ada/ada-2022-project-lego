import requests
import time
from tqdm import tqdm

import pandas as pd
import numpy as np
import os

data_folder = '../data/'
new_movie_metadata_fn = 'movie_list_revs.csv'

API_KEY = '29f483826286e7795c743d40e4b0f02e'
endpoint_url = 'https://api.themoviedb.org/3/'
req_details_general = f'discover/movie?api_key={API_KEY}&language=en-US&sort_by=revenue.desc&include_video=false%include_adult=false&with_runtime.gte=20'

movie_df = pd.DataFrame(columns=['movie_id','year', 'title'])
start_year = 1900
if os.path.exists(data_folder + new_movie_metadata_fn):
    movie_df = pd.read_csv(data_folder + new_movie_metadata_fn, index_col=0)
    start_year = movie_df['year'].max() + 1
    print(f"Found previous version with up to {start_year-1} ids scraped.")

print(f'Starting to scrape movie ids from TMDB, starting from {start_year}.')
for year in tqdm(range(start_year, 2022), total=2022-start_year):
    for page in range(1, 91):
        req_details = req_details_general + f'&year={year}&page={page}'
        response = requests.get(endpoint_url + req_details)
        if response.status_code == 200:
            data = response.json()
            if data['total_pages'] == 0 or data['total_pages'] < page:
                break
            for movie in data['results']:
                movie_df = pd.concat([movie_df, pd.DataFrame({'movie_id': [movie['id']], 'year': [year], 'title': [movie['title']]})], ignore_index=True)
        else:
            print(response.status_code)
            break
        
    movie_df.to_csv(data_folder + new_movie_metadata_fn)

