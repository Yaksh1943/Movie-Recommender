import streamlit as st
import pickle
import pandas as pd
import numpy as np





movies_list = pickle.load(open('movie_list.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
movies_list = movies_list['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender')

selected_movies_name = st.sidebar.selectbox(
    'Select Movie Recommender',
    movies_list
)
def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        # movie_id = movies[i[0]]
        #fetch poster id form tmdb api if require with id
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

if st.button('Recommend'):
    recommendation = recommend_movies(selected_movies_name)
    for i in recommendation:
        st.write(i)