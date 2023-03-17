
def getRecommendations(movie, rating, get_similar_movies, flash):
    try:
        returned_similar = get_similar_movies(movie, rating)
        stringified_df = returned_similar[0:15].to_string()
        stringified_df = stringified_df.split("\n")
        print(stringified_df)
        movies_array=[]
        for i in stringified_df:
            i = i.split("  ")[0]
            movies_array.append(i)
        similar_movies= movies_array[2:]
        result = {
            "similar_movies": similar_movies
        }
        return result
    except:
        return flash("Sorry, no suggestions.")