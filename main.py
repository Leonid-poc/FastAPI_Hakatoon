from pydantic import BaseModel
from typing import List, Optional
import fastapi

q = List[str]

class User(BaseModel):
    name: str
    age: int
    email: Optional[str]

app = fastapi.FastAPI(title="Testing")

@app.post('/')
def testing(user: User):
    return f'name - {user.name}, age - {user.age}, email - {user.email}'

# testing
# testing 2