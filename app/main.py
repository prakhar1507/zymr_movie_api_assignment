
from fastapi import FastAPI
from app.routes import movie_routes

app = FastAPI(
    title="Movie API",
    contact={
        "name": "Prakhar Srivastava",
        "email": "shrivastavaprakhar1507@gmail.com",  
    },
   
)


app.include_router(movie_routes.router, prefix="/movies", tags=["Movies"])
