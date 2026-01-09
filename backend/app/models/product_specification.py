from pydantic import BaseModel, Field

class Specification(BaseModel):
    name: str
    value: str