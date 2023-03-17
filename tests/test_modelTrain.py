import unittest
import pandas as pd
from controllers.utilities.model_training import get_similar_movies

class TestGetSimilarMovies(unittest.TestCase):

    def setUp(self):
        # Load test data
        self.user_rating = 3.5

    def test_get_similar_movies(self):
        # Test the function with a movie name and a user rating
        movie_name = 'avengers'
        similar_movies = get_similar_movies(movie_name, self.user_rating)
        
        # Assert that the output is a pandas Series
        self.assertIsInstance(similar_movies, pd.Series)
        
        # Assert that the output contains values
        self.assertGreater(len(similar_movies), 0)
        
if __name__ == '__main__':
    unittest.main()