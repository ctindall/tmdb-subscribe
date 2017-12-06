#!/usr/bin/env python

import tmdbsimple as tmdb
import json
import os

#slurp in config
config_file = open(os.path.expanduser("~/.tmdb-subscribe.json"), 'r')
config = json.load(config_file)
config_file.close()

tmdb.API_KEY = config['tmdb_api_key']
movies = tmdb.Movies()

print("fetching page 1");
response = movies.upcoming()
upcoming = response["results"]
print(response["total_pages"], " total pages");

for page in range(2,response["total_pages"] + 1):
    print("fetching page ", page);
    response = movies.upcoming(page=page)
    upcoming += response['results']

print(json.dumps(upcoming))
        



