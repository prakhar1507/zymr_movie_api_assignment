from app import models

_movies = []   
_counter = 1   


def save_movie(movie: models.Movie):
    global _counter
    movie.id = _counter
    _counter += 1
    _movies.append(movie)
    return movie


def get_all_movies():
    return _movies


def update_movie(movie_id: int, movie_data):
    for m in _movies:
        if m.id == movie_id:
            if movie_data.title is not None:
                m.title = movie_data.title
            if movie_data.director is not None:
                m.director = movie_data.director
            if movie_data.releaseYear is not None:
                m.releaseYear = movie_data.releaseYear
            if movie_data.genre is not None:
                m.genre = movie_data.genre
            if movie_data.rating is not None:
                m.rating = movie_data.rating
            return m
    return None


def delete_movie(movie_id: int):
    global _movies
    for m in _movies:
        if m.id == movie_id:
            _movies.remove(m)
            return {"message": "Movie deleted"}
    return {"message": "Movie not found"}
