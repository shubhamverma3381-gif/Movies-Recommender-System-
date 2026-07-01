import pickle
import urllib3
import requests
import pandas as pd
from flask import Flask, request, jsonify, send_from_directory
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__, static_folder='static', template_folder='static')

OMDB_API_KEY = '3aaaf806'

# Load data once at startup
movies_list = pd.read_pickle('movies.pkl')
similarity = pickle.load(open('similarity.pkl', 'rb'))

PLACEHOLDER = 'https://placehold.co/300x450/1a1a2e/gold?text=No+Poster'


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


def recommend(movie: str):
    idx = movies_list[movies_list['title'] == movie].index[0]
    distances = similarity[idx]
    top5 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [
        {'title': movies_list.iloc[i].title, 'poster': fetch_poster(movies_list.iloc[i].title)}
        for i, _ in top5
    ]


# ── Routes ──────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')


@app.route('/api/movies', methods=['GET'])
def get_movies():
    titles = movies_list['title'].tolist()
    return jsonify(titles)


@app.route('/api/recommend', methods=['POST'])
def api_recommend():
    data = request.get_json()
    movie = data.get('movie', '').strip()
    if not movie:
        return jsonify({'error': 'Movie title is required'}), 400
    if movie not in movies_list['title'].values:
        return jsonify({'error': 'Movie not found'}), 404
    try:
        results = recommend(movie)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000)