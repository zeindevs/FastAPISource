from app.schemas.base import BaseModel


class MovieSchema(BaseModel):
    movie_id: int
    title: str
    released: int
    rating: float
