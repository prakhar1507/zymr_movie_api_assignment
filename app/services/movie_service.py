from typing import List
from app import schemas


movies_db: List[schemas.MovieOut] = []
current_id = 1


def create_movie(movie: schemas.MovieCreate):
    global current_id
    new_movie = schemas.MovieOut(id=current_id, **movie.model_dump())
    movies_db.append(new_movie)
    current_id += 1
    return new_movie


def get_movies():
    """Return all movies"""
    return movies_db


def get_movie_by_id(movie_id: int):
    """Return a single movie by ID"""
    for movie in movies_db:
        if movie.id == movie_id:
            return movie
    return None  


def update_movie(movie_id: int, movie: schemas.MovieCreate):
    for i, m in enumerate(movies_db):
        if m.id == movie_id:
            updated_movie = schemas.MovieOut(id=movie_id, **movie.model_dump())
            movies_db[i] = updated_movie
            return updated_movie
    return {"error": "Movie not found"}


def delete_movie(movie_id: int):
    for i, movie in enumerate(movies_db):
        if movie.id == movie_id:
            del movies_db[i]
            return {"message": "Movie deleted successfully"}
    return {"error": "Movie not found"}
