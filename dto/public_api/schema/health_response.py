from pydantic import BaseModel


class HealthResponse(BaseModel):
    alive: bool
