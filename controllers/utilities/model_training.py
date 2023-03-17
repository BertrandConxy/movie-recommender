import pandas as pd

ratings = pd.read_csv('./datasets/ratings.csv')
movies = pd.read_csv('./datasets/movies.csv')

movies['title'] = movies['title'].str.lower()

# we basically need the rating and userID
# A DataFrame object has two axes: “axis 0” and “axis 1”. “axis 0” represents rows and “axis 1” represents columns
ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)

user_ratings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
# Let's drop/remove the movies which have less than 7 users who rated it and fill remaining NaN with 0
user_ratings = user_ratings.dropna(thresh=7,axis=1).fillna(0)

item_similarity_df = user_ratings.corr(method='pearson')
item_similarity_df.to_csv('./datasets/item_similarity_df.csv')

item_similarity_df = pd.read_csv('./datasets/item_similarity_df.csv', index_col=0)

def get_similar_movies(movie_name, user_rating):
    # subtract user_rating (used for scaling) by mean of rating to accomodate disliked movies
    similar_score = (item_similarity_df[movie_name]*(float(user_rating))-2.5)
    similar_movies = similar_score.sort_values(ascending=False)
    return similar_movies