from imdb import Cinemagoer
from tqdm import tqdm

import pandas as pd
import os

data_folder = '../data/'
movie_metadata_fn = 'movie_details_imdb.csv'
movie_details_fn = 'movie_details_cp.csv'


API_KEY = '29f483826286e7795c743d40e4b0f02e'
endpoint_url = 'https://api.themoviedb.org/3/'

movie_list = pd.read_csv(data_folder + movie_details_fn, index_col=0)

movie_df = pd.DataFrame(columns=['imdb_id', 'title', 'rating', 'votes', 'genres', 'plot_outline', 'plot', 'synopsis', 'certs'])
start_id = 0
if os.path.exists(data_folder + movie_metadata_fn):
    movie_df = pd.read_csv(data_folder + movie_metadata_fn, index_col=0)
    start_id = movie_df.shape[0]
    print(f"Found previous version with up to {start_id} id data scraped.")


ia = Cinemagoer()
print(f'Starting scraping movie details from TMDB, starting from {start_id}.')
for i, movie_id in tqdm(enumerate(movie_list['imdb_id']), total=movie_list.shape[0]):
    if i < start_id:
        continue
    if not isinstance(movie_id, str):
        print("bulshiiit", i)
        continue
    movie = ia.get_movie(int(movie_id[2:]))
    data = movie.data

    if not 'rating' in data.keys():
        continue
    for key in ['synopsis', 'plot outline', 'certificates', 'plot', 'genres']:
        if not key in data.keys():
            data[key] = '' 
    

    movie_df = pd.concat([movie_df, pd.DataFrame({'imdb_id': [movie_id], 'title': [data['localized title']], 'rating': [data['rating']], \
                                            'votes': [data['votes']], 'genres': [data['genres']],
                                            'plot_outline': [data['plot outline']], 'plot': [data['plot']], 
                                            'synopsis': [data['synopsis']], 'certs': [data['certificates']]})])

    if i%100 == 0:
        movie_df.to_csv(data_folder + movie_metadata_fn)

