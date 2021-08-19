from pydantic import BaseModel, ValidationError

class MultipleJokesRequestParams(BaseModel):
    count: int
