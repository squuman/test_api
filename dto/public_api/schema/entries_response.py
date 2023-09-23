from pydantic import BaseModel


class Entry(BaseModel):
    API: str
    Description: str
    Auth: str
    HTTPS: bool
    Cors: str
    Link: str
    Category: str


class EntriesResponse(BaseModel):
    count: int
    entries: list[Entry]
