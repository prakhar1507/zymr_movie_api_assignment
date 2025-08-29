from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class MovieCreate(BaseModel):
    title: str = Field(..., min_length=1)
    director: Optional[str] = None
    releaseYear: Optional[int] = None
    genre: Optional[str] = None
    rating: Optional[float] = Field(None, ge=1, le=10)


class MovieUpdate(MovieCreate):
    pass


class MovieOut(MovieCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)  

from pydantic import BaseModel

class MovieIn(BaseModel):
    """Schema for creating a movie"""
    title: str
    director:str
    releaseYear:int 
    genre:str
    rating: int

class MovieOut(MovieIn):
    """Schema for returning movie details"""
    id: int
