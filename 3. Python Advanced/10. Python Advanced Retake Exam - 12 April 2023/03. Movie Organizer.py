def movie_organizer(*args):
    movies = {}
    for movie, genre in args:
        if genre not in movies:
            movies[genre] = []
        movies[genre].append(movie)
    
    result = ""
    sorted_genres = sorted(movies, key=lambda g: (-len(movies[g]), g))
    
    for genre in sorted_genres:
        num_movies = len(movies[genre])
        result += f"{genre} - {num_movies}\n"
        sorted_movies = sorted(movies[genre])
        for movie in sorted_movies:
            result += f"* {movie}\n"
    
    return result[:-1]




print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))