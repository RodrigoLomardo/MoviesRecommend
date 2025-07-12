from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Carregar dataset
path = "ml-latest-small/"
movies = pd.read_csv(path + "movies.csv")
ratings = pd.read_csv(path + "ratings.csv")

# Troca o pipe por vazios
movies['genres'] = movies['genres'].str.replace('|', '', regex=False)

# vetorizar os gêneros
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

# calculando a similaridade do cosseno
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Índice auxiliar com títulos em minúsculas para facilitar a busca
movies['title_lower'] = movies['title'].str.lower()
indices = pd.Series(
    movies.index, index=movies['title_lower']).drop_duplicates()


# Função de recomendação com busca flexível (ignora maiúsculas/minúsculas)
def recommend(title, num_recommendations=5):
    title = title.lower().strip()

    # Buscar correspondência parcial nos títulos
    match = movies[movies['title_lower'].str.contains(title, na=False)]

    if match.empty:
        return f"Filme '{title}' não encontrado no dataset."

    # Usa o primeiro resultado correspondente
    idx = match.index[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations + 1]

    movie_indices = [i[0] for i in sim_scores]

    return movies['title'].iloc[movie_indices].tolist()


# Rotas flask
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_route():
    data = request.get_json()
    movie_title = data.get('movie', '')
    
    if not movie_title:
        return jsonify({'error': 'Título do filme não fornecido.'})

    recommendations = recommend(movie_title)

    if isinstance(recommendations, str):  # Se for a mensagem de erro
        return jsonify({'error': recommendations})
    
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)