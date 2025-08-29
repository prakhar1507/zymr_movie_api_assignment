from pydantic import BaseModel
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None   
    title: str
    director: Optional[str] = None
    releaseYear: Optional[int] = None
    genre: Optional[str] = None
    rating: Optional[float] = None
