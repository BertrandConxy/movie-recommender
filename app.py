import secrets
from flask import Flask, flash, request, render_template
from controllers.utilities.model_training import get_similar_movies
from controllers.movie_controller import getRecommendations

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)

# root api direct to index.html (home page)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def recommend():
    input_array = [str(x) for x in request.form.values()]
    displayed_name = str(input_array[0])
    movie_name = str(input_array[0]).lower()
    movie_rating = float(input_array[1])
    output = getRecommendations(movie_name, movie_rating, get_similar_movies, flash)
    if isinstance(output, dict):
        recommended_movies = output.get('similar_movies', [])
    else:
        recommended_movies = []
        flash(output) # use the flash function to display the error message to the user
    return render_template('index.html', recommended_movies=recommended_movies, searched_movie=displayed_name)

if __name__ == "__main__":
    app.run(debug=True)
