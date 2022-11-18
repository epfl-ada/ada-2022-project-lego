import requests
import time
from tqdm import tqdm

import pandas as pd
import numpy as np
import os

data_folder = '../data/'
movie_metadata_fn = 'MovieSummaries/movie.metadata.tsv'

plot_summaries_fn = 'MovieSummaries/plot_summaries.txt'

new_movie_metadata_fn = 'MovieSummaries/movie.metadata_extended.csv'
id_mapping_fn = 'fb2w.nt'

print("Starting id scraping.")

movie_df_noisy = pd.read_csv(data_folder + movie_metadata_fn, sep='\t', header=None)
plot_sums_df = pd.read_csv(data_folder + plot_summaries_fn, sep='\t', header=None)

df_movies_sums= movie_df_noisy.copy()
df_movies_sums = df_movies_sums.merge(plot_sums_df, on=[0])

movie_df = df_movies_sums[[0,'1_x',2,4]].copy()
movie_df.columns = ['movie_id', 'freebase_id', 'movie_name', 'revenue']

print(f"Got {movie_df.shape[0]} ids to scrape.")

max_i = 0
if os.path.exists(data_folder + new_movie_metadata_fn):
    movie_df_new = pd.read_csv(data_folder + new_movie_metadata_fn, index_col=0)

    movie_df['wiki_id'] = movie_df_new['wiki_id']
    movie_df['imdb_id'] = movie_df_new['imdb_id']
    movie_df['tmdb_id'] = movie_df_new['tmdb_id']
 
    for i, imdb_id in enumerate(movie_df['imdb_id']):
        if not imdb_id is np.NaN:
            max_i = i
    print(f"Found previous version with {max_i} ids scraped.")
else:
    # create freebase id to wikipedia id mapping
    with open(data_folder + id_mapping_fn) as f:
        lines = f.readlines()
    lines = lines[4:]

    id_map = {}

    for line in lines:
        line = line.split('\t')
        fbid = '/' +  line[0].split('/')[-1][:-1].replace('.', '/')
        wikiid = line[2][1:-4].split('/')[-1].strip()
        id_map[fbid] = wikiid

    #make columns out of mappings and rename the columns
    movie_df['wiki_id'] = movie_df['freebase_id'].map(id_map)

    movie_df['imdb_id'] = np.NaN
    movie_df['tmdb_id'] = np.NaN

endpoint_url = 'https://query.wikidata.org/sparql'

for i, wiki_id in tqdm(enumerate(movie_df['wiki_id']), total=movie_df.shape[0]):
    if i < max_i:
        continue
    if i % 200 == 0:
        movie_df.to_csv(data_folder + new_movie_metadata_fn)  
    if wiki_id is np.NaN:
        continue
    query = '''
        SELECT ?link_imdb ?link_tmdb
        WHERE{
        wd:''' + wiki_id + ''' wdt:P345 ?link_imdb;
        wdt:P4947 ?link_tmdb .
        }
    '''
    r = requests.get(endpoint_url, params = {'format': 'json', 'query': query})
    data = r.json()

    if len(data['results']['bindings']) == 0:
        continue
    
    imdb_id = data['results']['bindings'][0]['link_imdb']['value']
    tmdb_id = data['results']['bindings'][0]['link_tmdb']['value']
    movie_df.loc[i, 'imdb_id'] = imdb_id
    movie_df.loc[i, 'tmdb_id'] = tmdb_id
    time.sleep(2)
