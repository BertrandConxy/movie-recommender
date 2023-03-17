import unittest
import pandas as pd
from controllers.movie_controller import getRecommendations

class TestRecommendations(unittest.TestCase):
    
    def test_getRecommendations(self):
        # create a sample dataframe
        movies = ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"]
        ratings = [3.5, 4.0, 4.5, 3.0, 4.0]
        df = pd.DataFrame({"movie": movies, "rating": ratings})

        # define a mock get_similar_movies function
        def mock_get_similar_movies(movie, rating):
            return df[df["rating"] >= rating].sort_values(by="rating", ascending=False)

        # test the getRecommendations function with sample data
        result = getRecommendations("Movie A", 3.0, mock_get_similar_movies, lambda x: "Sorry, no suggestions.")

        # assert the expected result
        expected_result = {"similar_movies": ["Movie B", "Movie C", "Movie E"]}
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
