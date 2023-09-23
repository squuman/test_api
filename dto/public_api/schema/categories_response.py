from pydantic import BaseModel


class CategoriesResponse(BaseModel):
    count: int
    categories: list[str]
