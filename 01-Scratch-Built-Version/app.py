import pickle
import urllib3
import requests
import streamlit as st
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

OMDB_API_KEY = '3aaaf806'  # Step 1 dekho neeche

movies_list = pd.read_pickle('movies.pkl')
similarity = pickle.load(open('similarity.pkl', 'rb'))

PLACEHOLDER = 'https://placehold.co/300x450?text=No+Poster'

@st.cache_data
def fetch_poster(movie_title: str) -> str:
    try:
        url = f'https://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}'
        response = requests.get(url, timeout=10, verify=False)
        data = response.json()
        poster = data.get('Poster')
        if poster and poster != 'N/A':
            return poster
    except Exception:
        pass
    return PLACEHOLDER

@st.cache_data
def recommend(movie: str):
    idx = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[idx]
    top5 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [
        {'title': movies_list.iloc[i].title, 'poster': fetch_poster(movies_list.iloc[i].title)}
        for i, _ in top5
    ]

st.title('Movie Recommender System')

selected = st.selectbox('Search your favourite here', movies_list['title'].values)

if st.button('Recommend'):
    results = recommend(selected)
    cols = st.columns(5)
    for col, movie in zip(cols, results):
        col.image(movie['poster'], use_container_width=True)
        col.caption(movie['title'])