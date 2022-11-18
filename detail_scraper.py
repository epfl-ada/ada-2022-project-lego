import requests
from tqdm import tqdm

import pandas as pd
import os

data_folder = '../data/'
movie_metadata_fn = 'movie_details_c3.csv'
movie_list_fn = 'movie_list_ext.csv'

API_KEY = '29f483826286e7795c743d40e4b0f02e'
endpoint_url = 'https://api.themoviedb.org/3/'

movie_list = pd.read_csv(data_folder + movie_list_fn, index_col=0)

movie_df = pd.DataFrame(columns=['tmdb_id','r_date', 'imdb_id', 'runtime', 'revenue', 'budget','tmdb_plot', 'tmdb_certs',])
start_id = 0
if os.path.exists(data_folder + movie_metadata_fn):
    movie_df = pd.read_csv(data_folder + movie_metadata_fn, index_col=0)
    start_id = movie_df.shape[0]
    print(f"Found previous version with up to {start_id} id data scraped.")

print(f'Starting scraping movie details from TMDB, starting from {start_id}.')
for i, movie_id in tqdm(enumerate(movie_list['movie_id']), total=movie_list.shape[0]):
    if i < start_id:
        continue

    req_det1 = f'movie/{movie_id}?api_key={API_KEY}&language=en-US'
    req_det2 = f'movie/{movie_id}/release_dates?api_key={API_KEY}'


    response1 = requests.get(endpoint_url + req_det1)
    if response1.status_code != 200:
        continue

    data = response1.json()
    if data['imdb_id'] == '' or not data['imdb_id']:
        continue

    response2 = requests.get(endpoint_url + req_det2)
    if response2.status_code != 200:
        certs = "[]"
    else:
        certs = response2.json()['results']
        
    plot = data['overview'].replace('\n', ' ') if '\n' in data['overview'] else data['overview']
    movie_df = pd.concat([movie_df, pd.DataFrame({'tmdb_id': [data['id']], 'r_date': [data['release_date']], \
                                                'imdb_id': [data['imdb_id']], 'runtime': [data['runtime']], \
                                                'revenue': [data['revenue']], 'budget': [data['budget']],
                                                'tmdb_plot': [plot], 'tmdb_certs': [certs], })])

    if i%200 == 0:
        movie_df.to_csv(data_folder + movie_metadata_fn)

