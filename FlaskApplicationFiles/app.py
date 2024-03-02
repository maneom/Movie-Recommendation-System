from flask import Flask, render_template, url_for, request
import pickle
import numpy as np
import difflib
import pandas as pd

popular_movies  = pickle.load(open('popular_movies.pkl', 'rb'))
movie_list      = pickle.load(open('movie_list.pkl', 'rb'))
df              = pickle.load(open('df.pkl', 'rb'))
simillarity     = pickle.load(open('simillarity.pkl', 'rb'))
types_of_genres = pickle.load(open('types_of_genres.pkl','rb'))
genres_data     = pickle.load(open('genres_data.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def homePage():
    return(render_template('index.html',
                            types_of_genres = types_of_genres
                        ))

@app.route('/popularMovies')
def famous_movies():
    return(render_template('popularMovies.html',
                            image_url = list(popular_movies['poster_path'].values),
                            title     = list(popular_movies['title'].values),
                            wiki_link = list(popular_movies['wiki_link'].values),
                            rating    = list(popular_movies['imdb_rating'].values),
                            votes     = list(popular_movies['imdb_votes'].values)
                        ))

@app.route('/recommendMovies', methods=['POST', 'GET'])
def search_movies():
    if (request.method == 'POST'):
        movie_name = request.form['movie_name']
        movie_name = difflib.get_close_matches(movie_name,movie_list)
        if(len(movie_name)!=0):
            movie_name = movie_name[0]
            movie_index = df[df['title'] == movie_name].index[0]
            cosine_distance = simillarity[movie_index]
            required_movies = sorted(enumerate(cosine_distance),reverse=True, key=lambda x:x[1])[0:20]
            title = []
            summary = []
            actors = []
            wikipedia = []
            img_url = []
            for i in required_movies:
                title.append(df[df['imdb_id'] == df.iloc[i[0]]['imdb_id']]['title'].values[0])
                summary.append(" ".join(df[df['imdb_id'] == df.iloc[i[0]]['imdb_id']]['summary'].values[0]))
                actors.append(df[df['imdb_id'] == df.iloc[i[0]]['imdb_id']]['actors'].values[0])
                wikipedia.append(df[df['imdb_id'] == df.iloc[i[0]]['imdb_id']]['wiki_link'].values[0])
                img_url.append(df[df['imdb_id'] == df.iloc[i[0]]['imdb_id']]['poster_path'].values[0])
            return(render_template('recommendMovies.html',
                                    title = title,
                                    summary = summary,
                                    actors = actors,
                                    wiki_link = wikipedia,
                                    image_url = img_url,
                                    msg = "MOVIE NOT FOUND"
                                    ))
        else:
            return(render_template('recommendMovies.html',msg = "MOVIE NOT FOUND"))
    
    return(render_template('recommendMovies.html'))

@app.route('/genres/<type>')
def movies_based_on_genres(type):
    mov_list = genres_data[genres_data[type]==1].index
    title = []
    actors = []
    wikipedia = []
    img_url = []
    genres = []
    for i in range(len(mov_list)):
        
        img_url.append(df[df['title'] == mov_list[i]]['poster_path'].values[0])
        title.append(df[df['title'] == mov_list[i]]['title'].values[0])
        actors.append(df[df['title'] == mov_list[i]]['actors'].values[0])
        wikipedia.append(df[df['title'] == mov_list[i]]['wiki_link'].values[0])
        genres.append(df[df['title'] == mov_list[i]]['genres'].values[0])
        
    return(render_template('genresPage.html',
                            title       = title,
                            actors      = actors,
                            wiki_link   = wikipedia,
                            image_url   = img_url,
                            genres      = genres
                        ))

if __name__ == '__main__':
    app.run(debug=True)