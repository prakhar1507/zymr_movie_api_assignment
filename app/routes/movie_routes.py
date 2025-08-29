from fastapi import APIRouter
from app import schemas
from app.services import movie_service  
from fastapi import HTTPException



router = APIRouter()

@router.post("/", response_model=schemas.MovieOut, summary="Create a new movie", tags=["Movies"])
def create_movie(movie: schemas.MovieIn):
    """
    Create a new movie in the system.  
    - **id** is auto-generated
    - **title** (required): Title of the movie  
    - **director** : Name of the director  
    - **releaseYear**: Year of release (e.g., 1994)  
    - **genre**: Genre of the movie  
    - **rating**: Rating between 1 and 10"""  
    return movie_service.create_movie(movie)


@router.get("/", response_model=list[schemas.MovieOut], summary="List all movies", tags=["Movies"])
def get_movies():
    """Retrieve a list of all movies in the database."""
    return movie_service.get_movies()


@router.get("/{movie_id}", response_model=schemas.MovieOut, summary="Get a movie by ID", tags=["Movies"])
def get_movie(movie_id: int):
    """
    Retrieve a single movie by its ID.
    
    - **movie_id**: The ID of the movie you want to fetch  
    """
    movie=movie_service.get_movie_by_id(movie_id)
    if movie:
        return movie
    raise HTTPException(status_code=404, detail="Movie not found")


@router.put("/{movie_id}", response_model=schemas.MovieOut, summary="Update a movie", tags=["Movies"])
def update_movie(movie_id: int, movie: schemas.MovieIn):
    """
    Update an existing movie.
     
    """
    return movie_service.update_movie(movie_id, movie)


@router.delete("/{movie_id}", summary="Delete a movie", tags=["Movies"])
def delete_movie(movie_id: int):
    """
    Delete a movie by its ID.
     
    """
    return movie_service.delete_movie(movie_id)
