from pydantic import BaseModel, validator

#inputi type validation
class MultipleJokesRequestParams(BaseModel):
    count: int

    #in range validation
    @validator('count')
    def is_in_range(cls, value):
        if value not in range(1,11):
            raise ValueError("Out of range! Try 1 to 10.")
        return value
